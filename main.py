import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

should_continue = True
while should_continue:
    data_DF = pandas.DataFrame(data)
    phonetic_dict = {row.letter: row.code for (index, row) in data_DF.iterrows()}

    user_word = input("Enter the name?: ").upper()
    try:
        nato_list = [phonetic_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the alphabet are allowed")
    else:
        print(nato_list)
        
