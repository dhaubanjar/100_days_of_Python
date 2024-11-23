import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

user_input = input("Enter a word: ").upper()

compare_with_repeats = {index: phonetic_dict[letter] for index, letter in enumerate(user_input)}
print(compare_with_repeats)