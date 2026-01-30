
"""
The following program will require internet connection to run
"""
import goslate
import tkinter as tk
from tkinter import *


text = input("Please, input the text you want to translate: ")
language = str(input("Please, input the short code of the language you want to translate to(e.g EN): "))
text1 = goslate.Goslate()
trans_text = text1.translate(text, language)

print(trans_text)

# GUI
gui = tk.Tk()
gui.title("Text Translator")
gui.config(bg="black")



gui.mainloop()
