# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass


# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas
nato_path = r"26_Day\nato_phonetic_alphabet.csv"

nato_alphabet_df = pandas.read_csv(nato_path)

nato_dict = {row.letter:row.code for (index, row) in nato_alphabet_df.iterrows()}


def generate_phonetic():
    user_name = input("Enter your name: ").upper()
    try:
        op_list = [nato_dict[letter] for letter in user_name]
    except KeyError as kerror:
        print("Sorry only letters in alphabet please.")
        generate_phonetic()
    else:
        print(op_list)

generate_phonetic()
