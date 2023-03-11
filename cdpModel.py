# Machine learning using the connectionist dual process (CDP+) model
# to learn how to translate words to phonemes. The spelling of a word
# is learns to identify grapheme patterns which connect to phonemes.

import pandas as pd 
from buttonFunctions import colorResultButtons

# helper function gets the position of the onset letters
def getGrapheme(text):
    text = text.lower()

    # eɪ
    bigA = ["a*d","ea","ai", "eigh", "ay", "ey", "a", "ei"]
    smallA = []
    # for char in text
    onset = []
    vowel = []
    coda = []
    while len(text) % 5 != 0:
        text.append("*")
    orthographicVowels = ["a","e","i","o","u"]
    for char in text:
        for vowel in orthographicVowels:
            if char == vowel:
                vowel.append(char)
            else:
                onset.append(char)




# TODO: translation function
def getTranslation(text):
    #onset = getGrapheme(text)


    result = ""
    dataset = pd.read_csv("trainingAssets\English_Training.csv")
    X = dataset.drop(columns = ["phonetic"])
    y = dataset["phonetic"]
    
    
    colorResultButtons(result)
    return result
