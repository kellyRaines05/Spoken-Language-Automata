# Machine learning using the connectionist dual process (CDP+) model
# to learn how to translate words to phonemes. The spelling of a word
# is learns to identify grapheme patterns which connect to phonemes.

from buttonFunctions import colorResultButtons


# TODO: translation function
def getTranslation(text):
    phonemeList = ["t","ʌ","b"]
    result = ""
    for phoneme in phonemeList:
        result += phoneme
    #data = pd.DataFrame(pd.read_csv("C:\Users\kelly\OneDrive\Documents\CDP Training.xlsx"))
    colorResultButtons(phonemes = phonemeList)
    
    return result
