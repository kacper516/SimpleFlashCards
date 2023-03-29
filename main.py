import tkinter  # to make a gui app
import pandas  # to read from csv file
import random  # to generate random cards

BACKGROUND_COLOR = "#B1DDC6"
card = None
SOURCE_LANGUAGE = "English"
TRANSLATE = "Polish"
ORIGINAL_DATA = pandas.read_csv("data/en_to_pl.csv")

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    flash_cards = ORIGINAL_DATA.to_dict(orient="records")
else:
    flash_cards = data.to_dict(orient="records")


def right_button():
    """This function will perform action when user click the right button"""
    global card, flash_cards

    # to keep watch which card user have to revise
    flash_cards.remove(card)
    data = pandas.DataFrame(flash_cards)
    data.to_csv("data/words_to_learn.csv", index=False)
    
    next_card()


def next_card():
    """This function will perform action when user click the wrong button"""
    global card
    card = random.choice(flash_cards)
    canvas.itemconfig(canvas_img, image=front_img)
    canvas.itemconfig(title, text=TRANSLATE, fill="black")
    canvas.itemconfig(word, text=card[TRANSLATE], fill="black")
    window.after(3000, change_card)


def change_card():
    """This function will execute after some delay"""
    global card
    canvas.itemconfig(canvas_img, image=background_img)
    canvas.itemconfig(title, text=SOURCE_LANGUAGE, fill="white")
    canvas.itemconfig(word, text=card[SOURCE_LANGUAGE], fill="white")


# main window
window = tkinter.Tk()
window.title("Test")
window.minsize()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

# importing photos
front_img = tkinter.PhotoImage(file="images/card_front.png")
background_img = tkinter.PhotoImage(file="images/card_back.png")
right_img = tkinter.PhotoImage(file="images/right.png")
wrong_img = tkinter.PhotoImage(file="images/wrong.png")

# create a canva
canvas = tkinter.Canvas(width=800, height=526)
canvas_img = canvas.create_image(400, 263, image=front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"), fill="black", text="")
word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"), fill="black", text="")
canvas.grid(row=0, column=0, columnspan=2)

# buttons
button_right = tkinter.Button(image=right_img, highlightthickness=0, command=right_button)
button_right.grid(row=1, column=0)

button_wrong = tkinter.Button(image=wrong_img, highlightthickness=0, command=next_card)
button_wrong.grid(row=1, column=1)

# to first generate a random card
next_card()

window.mainloop()
