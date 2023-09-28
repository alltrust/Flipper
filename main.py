import pandas as pd
import tkinter
import random

CARD_BCG = "#33BBC5"
WRONG_BTN = "#FF6969"
RIGHT_BTN = "#85E6C5"
MAIN_BCG = "#614BC3"
FONT = ("Courier", 38)
initial_start = True
original_word = None
translation = None

language_file = "freq_span.csv"
translations_df = pd.read_csv(language_file)
lang1, lang2 = translations_df.columns

# function to display word label with timer
# on GUI open, don't start timer, until x or check is clicked
# then the timer counts down until 0, which it then displays the translation
# user then clicks 'x' or 'y' to display the next word and restart the timer



def count_down(time=3):
    """Counts down the timer and displays the """

    countdownLabel["text"] = time

    if time > 0 :
        mainWindow.after(1000, count_down, time-1)
    elif time == 0:
        display_back()

def get_words():
    """Returns the word and its translation."""
    global original_word 
    global translation

    randomizer = random.randint(0, len(translations_df) - 1)
    translation, word = translations_df.iloc[randomizer]

    original_word = word
    translation = translation

# def get_translation_word():
#     """Returns the translation of the origin"""

def display_front():
    """Displays the front of the card- which is the original word."""
    get_words()
    word_label.config(text=original_word)
    cardCanvas.config(background=MAIN_BCG)

    # if not initial_start:
    count_down()



def display_back():
    """Displays the back of the card-which is the translated word"""
    
    word_label.config(text=translation)
    cardCanvas.config(background=CARD_BCG)
    


mainWindow = tkinter.Tk()
mainWindow.config(background=MAIN_BCG)
mainWindow.title("Language Learner")
mainWindow.minsize(width=600, height=500)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)

cardCanvas = tkinter.Canvas(mainWindow, width=300,
                            height=200, background=CARD_BCG)
cardCanvas.grid(row=1, column=1)
wordLabel_num = cardCanvas.create_text(150, 100, font=FONT)

buttonFrame = tkinter.Frame(mainWindow, background=MAIN_BCG)
buttonFrame.grid(row=2, column=1, sticky="ews")

countdownLabel = tkinter.Label(mainWindow, font=FONT)
countdownLabel.grid(row=0, column=2) 

word_label = tkinter.Label(mainWindow, font=FONT)
word_label.grid(row=0, column=3)


photoimgWrong = tkinter.PhotoImage(file="images/wrong.png")
buttonWrong = tkinter.Button(buttonFrame, image=photoimgWrong,
                             highlightthickness=0, command=display_front)
buttonWrong.pack(side="left")

photoimgRight = tkinter.PhotoImage(file="images/right.png")
buttonRight = tkinter.Button(buttonFrame, image=photoimgRight,
                             highlightthickness=0, command=display_front)
buttonRight.pack(side="right")


mainWindow.mainloop()
