import pandas as pd
import tkinter
import random
from PIL import Image, ImageTk

MAIN_BCG = "#614BC3"
FONT = ("Courier", 22)
initial_start = True
original_word = None
translation = None
timer= "3"


language_file = "freq_span.csv"
translations_df = pd.read_csv(language_file)

def get_words():
    """Returns the word and its translation."""
    global original_word 
    global translation

    randomizer = random.randint(0, len(translations_df) - 1)
    translation, word = translations_df.iloc[randomizer]

    original_word = word
    translation = translation


def display_front():
    """Displays the front of the card- which is the original word."""
    global timer
    mainWindow.after_cancel(timer)

    get_words()
 
    cardCanvas.itemconfig(card_title, text="English", fill="black")
    cardCanvas.itemconfig(card_word, text=original_word, fill="black")
    cardCanvas.itemconfig(card_side, image= new_front)
    timer = mainWindow.after(3000,display_back)


def display_back():
    """Displays the back of the card-which is the translated word"""
  
    cardCanvas.itemconfig(card_title, text="Spanish", fill= "white")
    cardCanvas.itemconfig(card_word, text=translation, fill="white")
    cardCanvas.itemconfig(card_side, image= new_back)


mainWindow = tkinter.Tk()
mainWindow.config(background=MAIN_BCG)
mainWindow.title("Flipper")
mainWindow["pady"] = 18

mainWindow.minsize(width=600, height=500)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)

height = 300
width = 400

front_img = Image.open("images/card_front.png")
resized_front_img = front_img.resize((width, height))
new_front = ImageTk.PhotoImage(resized_front_img)

back_img= Image.open("images/card_back.png")
resized_back_img = back_img.resize((width,height))
new_back = ImageTk.PhotoImage(resized_back_img)

cardCanvas = tkinter.Canvas(mainWindow, width=500,
                            height=350, background=MAIN_BCG, highlightthickness=0)
card_side = cardCanvas.create_image(250,175,image=new_front)
card_title = cardCanvas.create_text(250, 100,text="HELLO", font=FONT, fill="black")
card_word = cardCanvas.create_text(250, 175, text="Click to start", fill="black", font=("Courier", 38, "bold"))
cardCanvas.grid(row=1, column=1)

buttonFrame = tkinter.Frame(mainWindow, background=MAIN_BCG)
buttonFrame.grid(row=2, column=1, sticky="ews")

photoimgWrong = tkinter.PhotoImage(file="images/wrong.png")
buttonWrong = tkinter.Button(buttonFrame, image=photoimgWrong,
                             highlightthickness=0, command=display_front, background=MAIN_BCG)
buttonWrong.pack(side="left")

photoimgRight = tkinter.PhotoImage(file="images/right.png")
buttonRight = tkinter.Button(buttonFrame, image=photoimgRight,
                             highlightthickness=0, command=display_front, background=MAIN_BCG)
buttonRight.pack(side="right")

mainWindow.mainloop()
