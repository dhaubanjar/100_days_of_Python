from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word ={}                                # stores current random word, accessible globally
words = {}
try:
    data = pd.read_csv('./data/to_learn_spanish.csv')
except FileNotFoundError:
    original_data = pd.read_csv('./data/spanish.csv')
    words = original_data.to_dict('records')
else:
    words = data.to_dict(orient='records')
#--------------------------- Read CSV -------------------------------#
def next_card():                                # changes to next random card from the pandas list
    global current_word, flip_timer             # creates private variable to global, can be accessed from other func.
    window.after_cancel(flip_timer)             # if button clicked many times, flip_timer stays same and give old result
    current_word = random.choice(words)         # cancelling window.after will reset to current card.
    rand_spanish = current_word["spanish"]
    canvas.itemconfig(card_word, text = "Espanol")              # update
    canvas.itemconfig(card_word, text = rand_spanish)
    canvas.itemconfig(canvas_image, image = card_front_img)
    canvas.itemconfig(card_title, text="Espanol", font=("Arial", 40, "italic"), fill="black")
    canvas.itemconfig(card_word, text=f"{rand_spanish}", font=("Arial", 60, "bold"), fill="black")
    flip_timer=window.after(10000, func=flip_card)           # waits 3 sec and calls flip_card()

def flip_card():
    rand_english = current_word["english"]                  # retrieve parallel english word of current spanish word.
    canvas.itemconfig(canvas_image, image = card_back_img)
    canvas.itemconfig(card_title, text= "English", font = ("Arial", 40, "italic"), fill = "white")
    canvas.itemconfig(card_word, text =f"{rand_english}" ,font = ("Arial", 60, "bold"), fill = "white")


def known_word():
    words.remove(current_word)                  # removes the current word if known to user, ie tick button pressed.
    print(len(words))
    data = pd.DataFrame(words)
    data.to_csv("./data/to_learn_spanish.csv", index=False)
    next_card()



#--------------------------- UI SETUP -------------------------------#
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
""" Canvas """
canvas = Canvas(window, width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Espanol", font=("Arial", 40, "italic") , fill="black")
card_word = canvas.create_text(400, 263, text=f"Word", font=("Arial", 60, "bold"), fill="black" )
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

""" Buttons"""
right_img = PhotoImage(file="./images/right.png")          # assigns image location to a variable
wrong_img = PhotoImage(file="./images/wrong.png")

right_button = Button(image=right_img, highlightthickness=0, command=known_word)        # creates a button
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)

right_button.grid(column=0, row=1)                                  # places the button on the screen
wrong_button.grid(column=1, row=1)

next_card()

window.mainloop()