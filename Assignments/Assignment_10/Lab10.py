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
Program was printing every word and its frequency instead of just the top 10 or less,
fixed by adding a check to see if variable counter has increased beyond 10.
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
    #print(clean_words_list)
    return clean_words_list

def get_freq_dict(clean_words_list):
    freq_dict = {}
    for word in clean_words_list:
        if word not in freq_dict:
            freq_dict[word] = 1
        else:
            freq_dict[word] += 1
    #print(freq_dict)
    return freq_dict

def sort_freq_dict(freq_dict):
    sorted_freq_dict = {word:freq for word,freq in sorted(freq_dict.items(), key=lambda pair: pair[1], reverse=True)}
    #print(sorted_freq_dict)
    return sorted_freq_dict

def get_word_stats(sorted_freq_dict):
    occur_once = 0
    total_unique = 0
    for freq in sorted_freq_dict.values():
        if freq == 1:
            occur_once += 1
        total_unique += 1
    return occur_once,total_unique

def output(sorted_freq_dict,occur_once,total_unique):
    print('Most frequently used words')
    print('{:>2s}{:>15s}{:>20s}'.format('#','Word','Freq.'))
    print('='*37)
    counter = 1
    for word in sorted_freq_dict:
        print('{:>2d}{:>15s}{:>20d}'.format(counter,word,sorted_freq_dict[word]))
        counter+=1
        if counter == 11:
            break
    print('\nThere are {} words that occur only once'.format(occur_once))
    print('There are {} unique words in the document'.format(total_unique))


file_name = get_file_name()

clean_words_list = file_to_clean_words_list(file_name)

freq_dict = get_freq_dict(clean_words_list)

sorted_freq_dict = sort_freq_dict(freq_dict)

occur_once, total_unique = get_word_stats(sorted_freq_dict)

output(sorted_freq_dict,occur_once,total_unique)