'''
CS 101 Lab
Program 6
Levi Lindskog is my name in Canvas, but I go by Levi Estabrook.
lhl8r5@umsystem.edu

PROBLEM:
Program loop must be able to allow user to choose between encoding a string in Caesar Cipher,
decoding a Caesar Cipher, or quitting out of the program.
When encrypting, program must ask user to input their string,
as well as an integer for how many places they want to move over in the Caesar Cipher.
When decrypting, program must ask user to input their encrypted string,
as well as an integer for how many places to move over in the Cipher.

ERROR HANDLING:
Decryption function wasn't working, fixed by swapping find() method with rfind method().

'''

#ALGORITHM

import string

def menu():

    print("MAIN MENU:\n1) Encode a string\n2) Decode a string\nQ) Quit")

    while True:
        
        selection = input('Enter your selection ==> ').strip().upper()

        if selection == '1':
            return 1
        elif selection == '2':
            return 2
        elif selection == 'Q':
            return None
        else:
            print('Invalid Entry.')


def Encryption():

    user_str_E = input('\nEnter (brief) text to encrypt: ').upper()

    translation = int(input('Enter the number to shift letters by: '))

    while not (0 <= translation < 26):
        if translation < 0:
            translation+=26
        elif translation >= 26:
            translation-=26
    
    encrypted_str = ''

    for index in range(len(user_str_E)):
        if user_str_E[index].isalpha():
            num = alpha_doubled.find(user_str_E[index])
            encrypted_str+=alpha_doubled[num + translation]
        else:
            encrypted_str+=user_str_E[index]

    print('Encrypted:', encrypted_str)
    print()


def Decryption():

    user_str_D = input('\nEnter (brief) text to decrypt: ').upper()

    translation = int(input('Enter the number to shift letters by: '))

    while not (0 <= translation < 26):
        if translation < 0:
            translation+=26
        elif translation >= 26:
            translation-=26
    
    decrypted_str = ''

    for index in range(len(user_str_D)):
        if user_str_D[index].isalpha():
            num = alpha_doubled.rfind(user_str_D[index])
            decrypted_str+=alpha_doubled[num - translation]
        else:
            decrypted_str+=user_str_D[index]
    
    print('Decrypted:', decrypted_str)
    print()

alpha_doubled = string.ascii_uppercase + string.ascii_uppercase

while True:

    selection = menu()

    if selection == 1:
        Encryption()
    elif selection == 2:
        Decryption()
    else:
        break