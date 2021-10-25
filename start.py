from TkinterGUI.graphicalUserInterface import GUI
from AI.game import AI
from tkinter import *


def start_gui():
    options_window.destroy()
    gui = GUI()
    gui.start()


def start_ai():
    options_window.destroy()
    ai = AI()
    ai.start()


options_window = Tk()
options_window.title("Game mode")
options_window.iconbitmap("C:/Users/paula/PycharmProjects/RockPaperScissors/scissors.ico")
options_window.config(bg='white')

screen_width = options_window.winfo_screenwidth()
screen_height = options_window.winfo_screenheight()
x = (screen_width / 2) - (400 / 2)  # make the main window pop on the middle of the screen
y = (screen_height / 2) - (200 / 2)
options_window.geometry(f'{400}x{200}+{int(x)}+{int(y)}')

main_frame = Frame(options_window, bg='white')
main_frame.pack(pady=30)

option_label = Label(main_frame, text='Choose game mode:', bg='white')
option_label.pack(pady=5)

tkinter_gui_button = Button(main_frame, text='TkinterGUI', bg='white', command=start_gui, width=15)
tkinter_gui_button.pack(pady=10)

ai_button = Button(main_frame, text='AI', bg='white', width=15, command=start_ai)
ai_button.pack(pady=5)

options_window.mainloop()
