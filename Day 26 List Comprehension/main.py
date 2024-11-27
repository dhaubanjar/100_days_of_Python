""" UPDATE: In Day 30, updated code using error handling."""
import pandas as pd

""" importing data from csv """
# nato = pd.read_csv('nato_phonetic_alphabet.csv')
# result = nato.set_index('letter').to_dict()['code']     # creating a dictionary
# print(result)

""" Second option """
nato = pd.read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {row.letter : row.code for (index, row) in nato.iterrows()}     # uses dictionary comprehension
def generate_phonetic():
    user_input = input("Enter a word. ").upper()
    try:
        compare = {n: phonetic_dict[n] for n in user_input}                             # uses dictionary comprehension
    except KeyError:
        print("Enter only letters.\n")
        generate_phonetic()
    else:
        print(compare)

generate_phonetic()