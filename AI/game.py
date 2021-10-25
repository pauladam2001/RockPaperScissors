from keras.models import load_model
import cv2
import numpy
import random


class AI:
    def __init__(self):
        self.reverse_objects_dict = {
            0: "rock",
            1: "paper",
            2: "scissors",
            3: "none"
        }

        self.model = load_model("C:/Users/paula/PycharmProjects/RockPaperScissors/AI/rock-paper-scissors-model.h5")

        self.capture = cv2.VideoCapture(0)
        self.capture.set(3, 1300)               # change window size
        self.capture.set(4, 1300)

        self.previous_move = None

    def mapper(self, value):                        # returns the sign associated to each number
        return self.reverse_objects_dict[value]

    @staticmethod
    def check_winner(player_choice, computer_choice):
        if player_choice == computer_choice:
            return "It's a tie!"
        elif player_choice == 'rock':
            if computer_choice == 'scissors':
                return 'Player wins!'
            else:
                return 'Computer wins!'
        elif player_choice == 'paper':
            if computer_choice == 'rock':
                return 'Player wins!'
            else:
                return 'Computer wins!'
        elif player_choice == 'scissors':
            if computer_choice == 'paper':
                return 'Player wins!'
            else:
                return 'Computer wins!'

    def start(self):
        while True:
            ret, frame = self.capture.read()        # 'read' a photo

            if not ret:
                continue

            cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 3)  # rectangle for user
            cv2.rectangle(frame, (800, 100), (1200, 500), (255, 255, 255), 3)  # rectangle for computer

            roi = frame[100:450, 100:450]
            img = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)  # extract the image from the user rectangle
            img = cv2.resize(img, (227, 227))

            pred = self.model.predict(numpy.array([img]))
            move_code = numpy.argmax(pred[0])  # predict the move made
            user_move_name = self.mapper(move_code)

            # computer move and check winner
            if self.previous_move != user_move_name:
                if user_move_name != "none":
                    computer_move_name = random.choice(['rock', 'paper', 'scissors'])
                    winner = self.check_winner(user_move_name, computer_move_name)
                else:
                    computer_move_name = "none"
                    winner = "Waiting..."
            self.previous_move = user_move_name

            # display the information
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, "Player's Move: " + user_move_name,
                        (50, 50), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(frame, "Computer's Move: " + computer_move_name,
                        (750, 50), font, 1.2, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(frame, "Winner: " + winner,
                        (400, 600), font, 2, (0, 255, 255), 4, cv2.LINE_AA)

            if computer_move_name != "none":  # insert an image in computer's rectangle
                icon = cv2.imread(
                    "C:/Users/paula/PycharmProjects/RockPaperScissors/AI/images/{}.png".format(computer_move_name))
                icon = cv2.resize(icon, (400, 400))
                frame[100:500, 800:1200] = icon

            cv2.imshow("Rock Paper Scissors", frame)

            k = cv2.waitKey(10)
            if k == ord('q'):  # press 'q' to exit
                break

        self.capture.release()
        cv2.destroyAllWindows()
