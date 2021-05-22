
"""
    NATO Phonetic Code Project

    Takes user input and give phonetic code for each alphabet in the word
"""


import pandas as pd

# Reads the NATO Phonetic Data
nato_alphabets = pd.read_csv("nato_phonetic_alphabet.csv")

# Converts pandas Dataframe into python dict
nato_dict = {row.letter:row.code for (index, row) in nato_alphabets.iterrows()}


def generate_phonetic():
    # Removes all the white spaces
    user_inp = input("Your name?").replace(" ", "")
    try:
        # Return the list based on user input
        phonetic_code = [nato_dict[letter] for letter in user_inp.upper()]
    except KeyError:
        print("Please write name in alphabets. Not in numbers")
        generate_phonetic()
    else:
        print(phonetic_code)


generate_phonetic()