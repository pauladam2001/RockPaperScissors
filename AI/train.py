import cv2
import numpy
from keras_squeezenet import SqueezeNet
from tensorflow.keras.optimizers import Adam
from keras.utils import np_utils
from keras.layers import Activation, Dropout, Convolution2D, GlobalAveragePooling2D
from keras.models import Sequential
import tensorflow
import os


IMAGE_DIRECTORY = 'image_data'

OBJECTS_DICT = {
    "rock": 0,
    "paper": 1,
    "scissors": 2,
    "none": 3
}

NUMBER_OF_ELEMENTS = len(OBJECTS_DICT)


def mapper(val):                            # returns the number associated to each sign
    return OBJECTS_DICT[val]


def get_model():
    model = Sequential([
        SqueezeNet(input_shape=(227, 227, 3), include_top=False),           # image with 227x227 pixels, 3 channels
        Dropout(0.5),                                                       # in order to prevent overfitting
        Convolution2D(NUMBER_OF_ELEMENTS, (1, 1), padding='valid'),
        Activation('relu'),             # rectified linear unit activation
        GlobalAveragePooling2D(),       # calculates the average output
        Activation('softmax')           # get the probabilities of each gesture
    ])
    return model


data_for_training = []                                        # load images from the directory
for directory in os.listdir(IMAGE_DIRECTORY):
    path = os.path.join(IMAGE_DIRECTORY, directory)
    if not os.path.isdir(path):
        continue
    for item in os.listdir(path):
        if item.startswith("."):
            continue
        image = cv2.imread(os.path.join(path, item))      # load the images in memory
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)      # convert the image from bgr to rgb
        image = cv2.resize(image, (227, 227))               # resize the image
        data_for_training.append([image, directory])                # directory = name of the gesture (rock, paper, scissors)

data, labels = zip(*data_for_training)        # unpack the data set, data = images, labels = rock, paper, scissors
labels = list(map(mapper, labels))  # map function, we pas the function that we want to apply and its parameter
                                    # map rock, paper.. with 0,1..

labels = np_utils.to_categorical(labels)

model = get_model()                         # define the model
model.compile(optimizer=Adam(lr=0.0001),        # Adam optimizer, learning rate 0.0001
              loss='categorical_crossentropy',  # display the loss
              metrics=['accuracy'],)            # in order for the accuracy to be displayed

# start training
model.fit(numpy.array(data), numpy.array(labels), epochs=10, batch_size=1)  # 10 iterations, epoch = full iteration over data set
                                                                            # batch_size - default is 32, so it will divide 800 (images) by 32
                                                                            # and in the epochs it will show only 25 instead of 800
model.save("rock-paper-scissors-model.h5")  # save the model because we will use it in the game
