from tkinter import *
from bs4 import BeautifulSoup as bs
import requests
import datetime

url = "https://www.merriam-webster.com/word-of-the-day"

# window
window = Tk()
window.geometry("1000x400")
window.title("Word Of The Day")
window.resizable(False, False)

page = requests.get(url)
soup = bs(page.text, "html.parser")

def past_words_cmd():
    words = []

    word = soup.find("h2", {"class":"word-header-txt"})
    word = word.string

    words.append(word)

    pw_window = Tk()
    pw_window.title("Past Words")

    pw_list_box = Listbox(pw_window, height = 17, font = "calibri 20 bold")

    for word in words:
        pw_list_box.insert(END, word)

    pw_list_box.grid()


    pw_window.mainloop()

def get_word():

    # Get word
    word = soup.find("h2", {"class":"word-header-txt"})
    word = word.string

    # Make a label to store word
    word_label = Label(master = window, text = word)
    word_label.config(font = "calibri 50 bold")
    word_label.grid(sticky = N, pady = 1, padx = 360)


def get_meaning():
    mean_frame = Frame(master = window)
    mean_txt = Label(master = mean_frame
                     , text = "What it mean?"
                     , font = "century 25"
                     , fg = "gray")
    
    mean_txt.grid()

    container = soup.find_all("div", class_= "wod-definition-container")[0]
    word = container.find("p").text

    mean = Label(master = mean_frame
                 ,text = word
                 ,font = "calibri 15"
                 ,wraplength = 1000)
    
    mean.grid()

    mean_frame.grid(sticky = W)

def get_date():
    # Get date
    date = datetime.date.today()
    year = date.year
    month = date.month
    day = date.day

    # make label for date
    date_label = Label(master = window, text = f"Word of the day: {month}-{day}-{year}")
    date_label.config(font = "arial 15", fg = "grey")
    date_label.grid(pady = 5)

def get_syl_pos():
    # get syl and pos
    syl = soup.find("span", {"class":"word-syllables"})
    pos = soup.find("span", {"class":"main-attr"})
    syl = syl.string
    pos = pos.string

    # make labels
    syl_pos_frame = Frame(master = window)

    syl_label = Label(master = syl_pos_frame, text = syl)
    pos_label = Label(master = syl_pos_frame, text = pos)
    syl_label.config(font = "arial 12 bold")
    pos_label.config(font = "arial 12 bold")
    syl_label.grid(row = 0, column = 0)
    Label(master = syl_pos_frame, text= "|", font = "calibri 12 bold").grid(row = 0, column = 1)
    pos_label.grid(row = 0, column = 2)
    syl_pos_frame.grid()

def past_words_button():
    past_words_button = Button(window, text = "Past Words", command = past_words_cmd)
    past_words_button.grid(sticky = NE)


    



#run
past_words_button()
get_date()
get_word()
get_syl_pos()
get_meaning()


window.mainloop()
