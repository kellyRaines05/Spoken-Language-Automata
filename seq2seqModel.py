from keras.models import Model
from keras.layers import Input, LSTM, Dense
from keras import callbacks
import pandas as pd
import numpy as np
import tensorflow as tf
import os

# suppress warning for AVX/FMA
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# use dataset language to train
data = pd.read_csv("trainingAssets/English_Training.csv")

# shuffle data for validation split
dataFrame = pd.DataFrame(data)
data = dataFrame.sample(frac = 1, random_state = 1).reset_index()

data = dataFrame.sample(10000)

data.to_csv("sampleEnglish.csv")

inputWordList = data['word'].astype(str).tolist()
output = data['phon'].astype(str).tolist()

# vectorize data with tab as the start sequence character and newline as the end sequence character
targetWordList = []
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

inputChars = sorted(list(inputChars))
targetChars = sorted(list(targetChars))
numEncodeToken = len(inputChars)
numDecodeToken = len(targetChars)

maxEncodeSeqLen = max([len(txt) for txt in inputWordList])
maxDecodeSeqLen = max([len(txt) for txt in targetWordList])

# preprocessing data to tokens
inputTokenIndex = dict([(char, i) for i, char in enumerate(inputChars)])
targetTokenIndex = dict([(char, i) for i, char in enumerate(targetChars)])

encoderInputData = np.zeros((len(inputWordList), maxEncodeSeqLen, numEncodeToken), dtype="float32")
decoderInputData = np.zeros((len(inputWordList), maxDecodeSeqLen, numDecodeToken), dtype="float32")
decoderTargetData = np.zeros((len(inputWordList), maxDecodeSeqLen, numDecodeToken), dtype="float32")

for i, (inputText, targetText) in enumerate(zip(inputWordList, targetWordList)):
    for t, char in enumerate(inputText):
        encoderInputData[i, t, inputTokenIndex[char]] = 1.0  
    
    for t, char in enumerate(targetText):
        # decoderTargetData is ahead of decoderInputData by one timestep
        decoderInputData[i, t, targetTokenIndex[char]] = 1.0
        if t > 0:
            # decoderTargetData will be ahead by one timestep (start character not included)
            decoderTargetData[i, t - 1, targetTokenIndex[char]] = 1.0

latentDim = 256
# define the input sequence as a sequence of characters
encoderInputs = Input(shape=(None, numEncodeToken))
encoderLSTM = LSTM(latentDim, return_state = True)
encoderOutputs, h, c = encoderLSTM(encoderInputs)
encoderStates = [h, c]

# define the output sequence as a sequence of IPA symbols
decoderInputs = Input(shape=(None, numDecodeToken))
decoderLSTM = LSTM(latentDim, return_sequences=True, return_state=True)
decoderOutputs, _, _ = decoderLSTM(decoderInputs, initial_state=encoderStates)
decoderDense = Dense(numDecodeToken, activation='softmax')
decoderOutputs = decoderDense(decoderOutputs)

# callback for early stopping, or when the model starts overfitting
callback = callbacks.EarlyStopping(monitor='accuracy', patience=10, restore_best_weights=True)

# define the model that will map inputs to outputs
model = Model([encoderInputs, decoderInputs], decoderOutputs)
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

# use GPU acceleration
with tf.device("/gpu:0"):
    model.fit([encoderInputData, decoderInputData], decoderTargetData, epochs = 100, batch_size = 30, callbacks = [callback], validation_split = 0.2)

model.save("englishModel")
model.summary()