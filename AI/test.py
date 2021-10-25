from keras.models import load_model
import cv2
import numpy
import sys

filepath = sys.argv[1]  # image path

REVERSE_OBJECTS_DICT = {
    0: "rock",
    1: "paper",
    2: "scissors",
    3: "none"
}


def mapper(val):                        # returns the sign associated to each number
    return REVERSE_OBJECTS_DICT[val]


model = load_model("rock-paper-scissors-model.h5")  # we use the trained model

image = cv2.imread(filepath)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = cv2.resize(image, (227, 227))

# pred = model.predict(numpy.array([img]))
# print(pred)

pred = model.predict(numpy.array([image]))
move_code = numpy.argmax(pred[0])
move_name = mapper(move_code)
print("Predicted: {}".format(move_name))  # in order to predict rock, paper, scissors, none instead of 0, 1, 2, 3
