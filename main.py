import pandas as pd

# Importing the phonetic words dat
df = pd.read_csv("nato_phonetic_alphabet.csv")

# creating a dictionary using dict comprehension where the key is the letter and value is the corresponding phonetic word
phonetic_dict = {row.letter: row.code for (index, row) in df.iterrows()}

# Getting User Input to generate the corresponding phonetic words
User_word = input("Enter a Word: ").upper()

# Generating the phonetic words for the corresponding letters from the word user gave using list comprehension
Phonetic_list = [phonetic_dict[i] for i in User_word]
print(Phonetic_list)
