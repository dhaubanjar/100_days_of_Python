# Phonetic Alphabet for any input word

import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

user_input = input("Enter a word: ").upper()

compare_with_repeats = [{letter: phonetic_dict[letter]} for  letter in user_input]
for item in compare_with_repeats:
    print(item)
