# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
import pandas as pd
#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     print(key)
#     print(value)

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     print('Student name', row['student'])
#     print('Student mark', row['score'])

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_spell = pd.read_csv('nato_phonetic_alphabet.csv')

nato_codes = {row['letter']:row['code'] for(index,row) in nato_spell.iterrows()}
#print(nato_codes)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
take_name = input('Please enter your name:').upper()


your_name = [nato_codes[letter] for letter in take_name]
print(your_name)

