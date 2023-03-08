# This project will utilize the International Phonetic Alphabet 
# to display the various translations from English, French, and
# German to IPA and light up the respective phonemes in the
# pronounciation of a word

from tkinter import *
from tkinter import ttk

# root pane
root = Tk()
root.title("Spoken Language Automata")
root.geometry("1200x800")
root.rowconfigure(0, weight = 1)
root.columnconfigure(0, weight = 1)
# root.configure(background="light blue") change color

# Instructions/ User input area
topBox = Frame(root)
topBox.grid(row = 0, column = 0, sticky= N)
topBox.rowconfigure(0, weight = 1)
topBox.columnconfigure(0, weight = 1)
topBox.columnconfigure(1, weight = 1)
topBox.columnconfigure(2, weight = 1)

# IPA Display area
bodyFrame = Frame(root, width = 1200, height = 800)
bodyFrame.grid(row = 0, column = 0)
bodyFrame.rowconfigure(0, weight = 1)
bodyFrame.columnconfigure(0, weight = 1)
bodyFrame.columnconfigure(1, weight = 1)
bodyFrame.columnconfigure(2, weight = 1)
bodyFrame.columnconfigure(3, weight = 1)
bodyFrame.columnconfigure(4, weight = 1)
bodyFrame.columnconfigure(5, weight = 1)

vowelBox = Frame(bodyFrame, relief= "ridge", borderwidth = 5, width = 600, height = 600)
vowelBox.grid(row = 0, column = 0, columnspan = 2, pady = 10, padx = 5, ipadx= 10, ipady= 10)
vowelBox.rowconfigure(0, weight = 1)
vowelBox.rowconfigure(1, weight = 1)
vowelBox.rowconfigure(2, weight = 1)
vowelBox.rowconfigure(3, weight = 1)
vowelBox.rowconfigure(4, weight = 1)
vowelBox.rowconfigure(5, weight = 1)
vowelBox.rowconfigure(6, weight = 1)
vowelBox.columnconfigure(1, weight = 1)
vowelBox.columnconfigure(2, weight = 1)
vowelBox.columnconfigure(3, weight = 1)
vowelBox.columnconfigure(0, weight = 1)


consonantBox = Frame(bodyFrame, relief = "ridge", borderwidth = 5, width = 600, height = 600)
consonantBox.grid(row = 0, column = 2, columnspan = 3, pady = 10, padx = 5, ipadx= 10, ipady= 10)
consonantBox.rowconfigure(0, weight = 1)
consonantBox.columnconfigure(2, weight = 1)


Label(topBox, text = "Please enter a word: ", font = "Times 12 bold").grid(row = 0, column = 0, pady = 5, sticky = N)
# user input
input = Text(topBox, height = 1, width = 80)
input.insert(END, "Type here...")
input.grid(row = 1, column = 0, padx = 5)

# drop down
dropDown = ttk.Combobox(topBox, state = "readonly", values = ["English", "French", "German"])
dropDown.set("Select Language...")

dropDown.grid(row = 1, column = 1, padx = 5)

# TODO: translation function
def getIPA():
    pass

# button initiates machine
enterButton = Button(topBox, text = "GO", command = getIPA)
enterButton.grid(row = 1, column = 2, padx = 5, ipadx = 10)

# phoneme (vowel and consonant box) contents
Label(vowelBox, text = "Vowel Phonemes", font = "Times 12 bold").grid(row = 0, column = 1, pady = 5, columnspan = 2)
Label(consonantBox, text = "Consonant Phonemes", font = "Times 12 bold").grid(row = 0, column = 0, pady = 5, columnspan = 2)


def placePhoneme():
    counter = 0
    vowelPhonemes = ["i","y","ɨ","ʉ","ɯ","u","ɪ","ʏ","ʊ","e","ø","ɘ","ɵ","ɤ","o","ə","ɛ","œ","ɜ","ɞ","ʌ","ɔ","æ","ɐ","a","ɶ","ɑ","ɒ"]
    consonantPhonemes = ["p","b","t","d","ʈ","ɖ","c","ɟ","k","ɡ","q","ɢ","ʔ","m","ɱ","n","ɳ","ɲ","ŋ","ɴ","ʙ","r","ʀ","ⱱ","ɾ","ɽ","ɸ",
                         "β","f","v","θ","ð","s","z","ʃ","ʒ","ʂ","ʐ","ç","ʝ","x","ɣ","χ","ʁ","ħ","ʕ","h","ɦ","ɬ","ɮ","ʋ","ɹ","ɻ","j",
                         "ɰ","l","ɭ","ʎ","ʟ","ʘ","ǀ","!","ǂ","ǁ","ɓ","ɗ","ʄ","ɠ","ʛ","ʍ","w","ɥ","ʜ","ʢ","ʡ","ɕ","ʑ","ɺ","ɧ"]
    for i in range(7):
        for j in range(4):
            vowel = vowelPhonemes[counter]
            newPhonemeButton = Button(vowelBox, text = vowel, width = 5, height = 5)
            newPhonemeButton.grid(row = j+1, column = i, pady = 5)
            counter += 1
    counter = 0
    for i in range(14):
        for j in range(6):
            consonant = consonantPhonemes[counter]
            newConsonantButton = Button(consonantBox, text = consonant, width = 5, height = 3)
            newConsonantButton.grid(row = j+1, column = i, pady = 5)
            counter += 1
            if counter == 79:
                break
    
placePhoneme()

# grid shows international phonetic alphabet
root.mainloop()