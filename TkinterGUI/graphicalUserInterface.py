from tkinter import *
import random
from PIL import Image, ImageTk
import pygame


class GUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Rock, paper, scissors")
        self.root.iconbitmap("C:/Users/paula/PycharmProjects/RockPaperScissors/scissors.ico")
        # self.root.config(bg='white')

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (800 / 2)  # make the main window pop on the middle of the screen
        y = (screen_height / 2) - (500 / 2)
        self.root.geometry(f'{800}x{500}+{int(x)}+{int(y)}')

        self.rock_image = ImageTk.PhotoImage(Image.open("C:/Users/paula/PycharmProjects/RockPaperScissors/TkinterGUI/images/rock.png"))
        self.paper_image = ImageTk.PhotoImage(Image.open("C:/Users/paula/PycharmProjects/RockPaperScissors/TkinterGUI/images/paper.png"))
        self.scissors_image = ImageTk.PhotoImage(Image.open("C:/Users/paula/PycharmProjects/RockPaperScissors/TkinterGUI/images/scissors.png"))
        self.start_image = ImageTk.PhotoImage(Image.open("C:/Users/paula/PycharmProjects/RockPaperScissors/TkinterGUI/images/waiting.png"))

        pygame.mixer.init()

    def player_computer_choice(self, player_choice):
        if player_choice == 'rock':
            self.player_image_label.configure(image=self.rock_image)
        elif player_choice == 'paper':
            self.player_image_label.configure(image=self.paper_image)
        else:
            self.player_image_label.configure(image=self.scissors_image)

        computer_choice = random.choice(['rock', 'paper', 'scissors'])

        if computer_choice == 'rock':
            self.computer_image_label.configure(image=self.rock_image)
        elif computer_choice == 'paper':
            self.computer_image_label.configure(image=self.paper_image)
        else:
            self.computer_image_label.configure(image=self.scissors_image)

        self.check_winner(player_choice, computer_choice)

    def player_score_update(self):
        score = int(self.player_score['text'])
        score += 1
        self.player_score['text'] = str(score)

    def computer_score_update(self):
        score = int(self.computer_score['text'])
        score += 1
        self.computer_score['text'] = str(score)

    def check_winner(self, player_choice, computer_choice):
        song = "C:/Users/paula/PycharmProjects/RockPaperScissors/TkinterGUI/sounds/fail.wav"
        if player_choice == computer_choice:
            self.victory_message['text'] = "It's a tie!"
            song = ''
        elif player_choice == 'rock':
            if computer_choice == 'scissors':
                self.victory_message['text'] = 'Player wins!'
                self.player_score_update()
                song = "C:/Users/paula/PycharmProjects/RockPaperScissors/TkinterGUI/sounds/win.wav"
            else:
                self.victory_message['text'] = 'Computer wins!'
                self.computer_score_update()
        elif player_choice == 'paper':
            if computer_choice == 'rock':
                self.victory_message['text'] = 'Player wins!'
                self.player_score_update()
                song = "C:/Users/paula/PycharmProjects/RockPaperScissors/TkinterGUI/sounds/win.wav"
            else:
                self.victory_message['text'] = 'Computer wins!'
                self.computer_score_update()
        elif player_choice == 'scissors':
            if computer_choice == 'paper':
                self.victory_message['text'] = 'Player wins!'
                self.player_score_update()
                song = "C:/Users/paula/PycharmProjects/RockPaperScissors/TkinterGUI/sounds/win.wav"
            else:
                self.victory_message['text'] = 'Computer wins!'
                self.computer_score_update()

        if song != '':
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()

    def reset_score(self):
        self.player_image_label.configure(image=self.start_image)
        self.computer_image_label.configure(image=self.start_image)
        self.victory_message['text'] = ''
        self.player_score['text'] = '0'
        self.computer_score['text'] = '0'

    def start(self):
        rock_button = Button(self.root, image=self.rock_image, border=3, command=lambda: self.player_computer_choice('rock'))
        rock_button.grid(row=4, column=1, padx=10, pady=10)
        paper_button = Button(self.root, image=self.paper_image, border=3, command=lambda: self.player_computer_choice('paper'))
        paper_button.grid(row=4, column=2)
        scissors_button = Button(self.root, image=self.scissors_image, border=3, command=lambda: self.player_computer_choice('scissors'))
        scissors_button.grid(row=4, column=3, padx=10)

        self.player_score = Label(self.root, text='0', font=('calibri', 23, 'bold'))
        self.player_score.grid(row=2, column=0)
        self.computer_score = Label(self.root, text='0', font=('calibri', 23, 'bold'))
        self.computer_score.grid(row=2, column=4)

        self.player_image_label = Label(self.root, image=self.start_image)
        self.player_image_label.grid(row=1, column=0)
        self.computer_image_label = Label(self.root, image=self.start_image)
        self.computer_image_label.grid(row=1, column=4)

        player_label = Label(self.root, text='Player', font=('calibri', 25, 'bold'))
        player_label.grid(row=0, column=0, pady=10)
        computer_label = Label(self.root, text='Computer', font=('calibri', 25, 'bold'))
        computer_label.grid(row=0, column=4)

        self.victory_message = Label(self.root, font=('calibri', 20, 'bold'))
        self.victory_message.grid(row=1, column=2)

        choice_label = Label(self.root, text="Player's choice", font=('calibri', 23, 'bold'))
        choice_label.grid(row=3, column=2)

        reset_score_button = Button(self.root, text='Reset score', font=('calibri', 15, 'bold'), command=self.reset_score)
        reset_score_button.grid(row=5, column=2, padx=15)

        self.root.mainloop()
