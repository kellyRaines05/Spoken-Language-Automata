from keras.models import load_model
import numpy as np
import pandas as pd

def getLanguageData(lang):
    # load the trained model
    model = load_model(lang + "Model")

    data = pd.read_csv("sample" + lang + ".csv")
    targetWordList = []
    inputWordList = data['word'].astype(str).tolist()
    output = data['phon'].astype(str).tolist()
    inputChars = set()
    targetChars = set()

    for word in output:
        target =  "\t" + word + "\n"
        targetWordList.append(target)

        for char in target:
            if char not in targetChars:
                targetChars.add(char)

    for word in inputWordList:
        for char in word:
            if char not in inputChars:
                inputChars.add(char)

    # define input and target token index dictionaries
    inputChars = sorted(list(inputChars))
    targetChars = sorted(list(targetChars))
    numEncodeToken = len(inputChars)
    numDecodeToken = len(targetChars)

    maxEncodeSeqLen = max([len(txt) for txt in inputWordList])
    maxDecodeSeqLen = max([len(txt) for txt in targetWordList])

    inputTokenIndex = dict([(char, i) for i, char in enumerate(inputChars)])

    return maxEncodeSeqLen, numEncodeToken, inputTokenIndex, targetChars, maxDecodeSeqLen, numDecodeToken, model

# function encodes user input to the required input format for the model
def encodeUserInput(inputText, language):
    maxEncodeSeqLen, numEncodeToken, inputTokenIndex, _, _, _, _ = getLanguageData(language)
    encoderInputData = np.zeros((1, maxEncodeSeqLen, numEncodeToken), dtype="float32")
    for t, char in enumerate(inputText):
        encoderInputData[0, t, inputTokenIndex[char]] = 1.0  
    return encoderInputData

# function decodes the predicted output into IPA symbols
def decodeIPA(output, language):
    _, _, _, targetChars, _, _, _ = getLanguageData(language)
    decodedOutput = ''
    for i in range(len(output)):
        sampledTokenIndex = np.argmax(output[i])
        sampledChar = targetChars[sampledTokenIndex]
        if sampledChar == '\n':
            break
        if sampledChar != '\t':
            decodedOutput += sampledChar
    return decodedOutput

def predict(encodedInput, language):
    _, _, _, _, maxDecodeSeqLen, numDecodeToken, model = getLanguageData(language)
    # predict IPA translation using the trained model
    output = model.predict([encodedInput, np.zeros((1, maxDecodeSeqLen, numDecodeToken))])

    # decode predicted output into IPA symbols
    predictedIPA = decodeIPA(output[0], language)

    return predictedIPA
