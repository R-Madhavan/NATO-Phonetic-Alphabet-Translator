import pandas

#Created a dictionary in this format {"A": "Alfa", "B": "Bravo, "C": "Charlie"}
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_DF = pandas.DataFrame(data)
phonetic_dict = {row.letter: row.code for (index, row) in data_DF.iterrows()}

#Created a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter the name?: ").upper()
nato_list = [phonetic_dict[letter] for letter in user_word]
print(nato_list)
