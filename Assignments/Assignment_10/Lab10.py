'''
CS 101 Lab
Program 10
Levi Lindskog is my name in Canvas, but I go by Levi Estabrook.
lhl8r5@umsystem.edu

PROBLEM:
Program must open a user inputted file using the open method using a try and except block.
Program must read file and use the split and strip functions
to make a list of the words in the file without any punctuation and spaces.
Program must keep track of how many times each word appears in file,
and store this information in a dictionary.
Proram must output to user the top ten most frequently used words and how many times they appear.
Program must output how many words occur only once,
and how many unique words there are total.

ERROR HANDLING:

'''

#ALGORITHM



def get_file_name():
    while True:
        try:
            user_input = input('Enter the name of the file to open ').strip()
            file = open(user_input)
            file.close()
            print()
            return user_input
        except FileNotFoundError:
            print('Could not open file', user_input)
            print('Please Try again\n')

def file_to_clean_words_list(file_name):
    with open(file_name) as file:
        words_list = file.read().split()
        clean_words_list = [word.strip(' .,!?:;-').lower() for word in words_list if len(word.strip(' .,!?:;-')) > 3]
    print(clean_words_list)
    return clean_words_list

def get_freq_dict(clean_words_list):
    freq_dict = {}
    for word in clean_words_list:
        if word not in freq_dict:
            freq_dict[word] = 1
        else:
            freq_dict[word] += 1
    print(freq_dict)
    return freq_dict



file_name = get_file_name()

clean_words_list = file_to_clean_words_list(file_name)

freq_dict = get_freq_dict(clean_words_list)