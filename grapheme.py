from g2p_en import G2p
import pandas as pd

g2p = G2p()

data = pd.read_csv("trainingAssets/English_Training.csv")
data.sample(frac = 1, random_state = 1).reset_index()

data = data.sample(5000)

words = data['word']

for word in words:
    phonemes = g2p(word)
    s = " ".join(phonemes)
    print("\nPhoneme:", s)