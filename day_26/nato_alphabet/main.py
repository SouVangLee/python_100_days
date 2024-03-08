import pandas as pd

nato_data_frame = pd.read_csv("nato_phonetic_alphabet.csv")

NATO_DICT = {
    row.letter: row.code
    for (index, row) in nato_data_frame.iterrows()
}

name = input("Enter a word: ").upper()

name_letters = [char for char in name]
name_dict = [NATO_DICT[letter] for letter in name_letters]

print(name_dict)
