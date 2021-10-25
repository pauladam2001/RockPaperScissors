import cv2  # for capturing image from webcam
import os
import sys


try:
    label_name = sys.argv[1]            # name of the folder that will be created (rock, paper, scissors, none)
    number_of_images = int(sys.argv[2])      # how many pictures the computer will take
except Exception:
    print("Arguments missing!")
    exit(-1)

IMAGE_DIRECTORY = 'image_data'                                    # the directory in which the folders will be
IMAGE_FOLDER = os.path.join(IMAGE_DIRECTORY, label_name)

try:
    os.mkdir(IMAGE_DIRECTORY)
except FileExistsError:
    pass
try:
    os.mkdir(IMAGE_FOLDER)
except FileExistsError:
    print("{} directory already exists!".format(IMAGE_FOLDER))
    print("All images gathered will be saved along with existing items in this folder!")

capture = cv2.VideoCapture(0)           # open the webcam

start = False
count = 0

while True:
    ret, frame = capture.read()         # 'read' a photo
    if not ret:
        continue

    if count == number_of_images:        # when we have enough samples we stop
        break

    # rectangle where the user will show the sign
    cv2.rectangle(frame, (100, 100), (450, 450), (255, 255, 255), 4)  # (450, 450) = size of rectangle, 4 = border

    if start:
        rectangle_image = frame[100:450, 100:450]   # take the image from the rectangle
        save_path = os.path.join(IMAGE_FOLDER, '{}.jpg'.format(count + 1))        # name the image
        cv2.imwrite(save_path, rectangle_image)     # write the image in the directory
        count += 1

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Collecting {}".format(count),                       # on screen it will appear how many images we collected
                (5, 50), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow("Collecting images", frame)      # window title

    key = cv2.waitKey(10)
    if key == ord('a'):               # when we press 'a' the collecting will start
        start = not start

    if key == ord('q'):               # when we press 'q' the program will end
        break

print("\n{} image(s) saved to {}".format(count, IMAGE_FOLDER))
capture.release()
cv2.destroyAllWindows()
