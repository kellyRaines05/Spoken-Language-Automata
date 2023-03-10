# These methods will automatically create the necessary 115 buttons
# which represent all phonemes from the IPA, sound is added to each
# on button press. Yellow color highlights the particular buttons/
# phonemes in the language.

from tkinter import *
from pygame import mixer
import time

# create an empty list for all the buttons
buttonList = []

# add sounds to button
mixer.init()
def play(phoneme):
    sound = mixer.Sound("phonemeAssets/" + phoneme + ".wav")
    return sound

# automatically create buttons of the phonemes and place into frame
def placePhoneme(vowelBox, consonantBox):
    counter = 0
    # list of all IPA phonemes
    vowelPhonemes = ["i","y","ɨ","ʉ","ɯ","u","ɪ","ʏ","ʊ","e","ø","ɘ","ɵ","ɤ","o","ə","ɛ","œ","ɜ","ɞ","ʌ","ɔ","æ","ɐ","a","ɶ","ɑ","ɒ"]
    consonantPhonemes = ["p","b","t","d","ʈ","ɖ","c","ɟ","k","ɡ","q","ɢ","ʔ","m","ɱ","n","ɳ","ɲ","ŋ","ɴ","ʙ","r","ʀ","ⱱ","ɾ","ɽ","ɸ",
                         "β","f","v","θ","ð","s","z","ʃ","ʒ","ʂ","ʐ","ç","ʝ","x","ɣ","χ","ʁ","ħ","ʕ","h","ɦ","ɬ","ɮ","ʋ","ɹ","ɻ","j",
                         "ɰ","l","ɭ","ʎ","ʟ","ʘ","ǀ","!","ǂ","ǁ","ɓ","ɗ","ʄ","ɠ","ʛ","ʍ","w","ɥ","ʜ","ʢ","ʡ","ɕ","ʑ","ɺ","ɧ", "dʒ",
                         "dz","ts","tʃ","tɕ","ʈʂ", "dʑ", "ɖʐ"]

    for i in range(7):
        for j in range(4):
            vowel = vowelPhonemes[counter]
            newPhonemeButton = Button(vowelBox, text = vowel, command = play(vowel).play, width = 5, height = 3, bg = "white")
            newPhonemeButton.grid(row = j+1, column = i, pady = 25, padx = 3)
            buttonList.append(newPhonemeButton)
            counter += 1
    
    counter = 0
    for i in range(15):
        for j in range(6):
            consonant = consonantPhonemes[counter]
            newConsonantButton = Button(consonantBox, text = consonant, command = play(consonant).play, width = 5, height = 3, bg = "white")
            newConsonantButton.grid(row = j+1, column = i, pady = 10, padx = 3)
            buttonList.append(newConsonantButton)
            counter += 1
            if counter == 87:
                break

# highlight the buttons that are in the particular language
def highlightButtons(dropDown):
    # create a list for each of the phonemes from the IPA that are included in each particular language
    englishPhoneme = ["p","b","t","d","k","ɡ","m","n","ŋ","f","v","θ","ð","s","z","ʃ","ʒ","tʃ","dʒ",
                    "w","h","ɹ","j","l","i","u","ɪ","ʊ","ə","ɛ","ɔ","æ","ɑ","ɒ","e","ʌ"]
    frenchPhoneme = ["p","b","t","d","k","ɡ","m","n","ɲ","ŋ","f","v","s","z","ʃ","ʒ","ʁ",
                    "w","l","j","ɥ","i","y","u","e","ø","o","ɛ","œ","ə","ɔ","a","ɑ"]
    germanPhoneme = ["p","b","t","d","k","ɡ","m","n","ŋ","f","v","ts","ð","s","z","ʃ","ʒ","tʃ","ʔ","dʒ","ç",
                    "x","r","h","j","l", "i","y","u","ɪ","e","ʏ","ø","ɛ","œ","ə","ɐ","a","ɔ","ʊ", "o"]
    
    # go through each button and recolor accordingly
    for button in buttonList:
        button.configure(bg = "white")
        
        if dropDown.get() == "English":
            for letter in englishPhoneme:
                if button["text"] == letter:
                    button.configure(bg = "yellow")
        if dropDown.get() == "French":
            for letter in frenchPhoneme:
                if button["text"] == letter:
                    button.configure(bg = "yellow")
        if dropDown.get() == "German":
            for letter in germanPhoneme:
                if button["text"] == letter:
                    button.configure(bg = "yellow")

    print("DONE")

def colorResultButtons(phonemes):
    colorButtonList = []
    for phoneme in phonemes:
        for button in buttonList:
            if button["text"] == phoneme:
                colorButtonList.append(button)

    for button in colorButtonList:
        #add delay here
        button.configure(bg = "green")
        button.invoke()