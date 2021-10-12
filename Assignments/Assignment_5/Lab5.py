'''
CS 101 Lab
Program 5
Levi Lindskog is my name in Canvas, but I go by Levi Estabrook.
lhl8r5@umsystem.edu

PROBLEM:
The Program must be able to ask for an ID input and determine whether it is a valid ID given the parameters.
The Program must check an inputted ID and intepret from it the school the student attends, and the year of school they're on.
The Program must be able to detect errors in ID inputs and return what is invalid about the ID.
The Program must be able to loop and take multiple IDs, and then close when the user inputs the enter key.


ERROR HANDLING:
Was getting wrong results from get_check_digit(ID) function,
fixed by multiplying character value by (index + 1).
Program thought check digit value didn't match even when it did,
fixed by comparing the returned value from get_check_digit(ID) to int(ID[9]),
where it was previously comparing to ID[9].
'''

#ALGORITHM

def get_school(ID):
    value = ID[5]
    if value == '1':
        return 'School of Computing and Engineering SCE'
    elif value == '2':
        return 'School of Law'
    elif value == '3':
        return 'College of Arts and Sciences'
    else:
        return 'Invalid School'


def get_grade(ID):
    value = ID[6]
    if value == '1':
        return 'Freshman'
    elif value == '2':
        return 'Sophopmore'
    elif value == '3':
        return 'Junior'
    elif value == '4':
        return 'Senior'
    else:
        return 'Invalid Grade'


def character_value(character):
    return ord(character.upper()) - 65


def get_check_digit(ID):
    total = 0
    for x in range(5):
        letter = character_value(ID[x])
        total += (letter * (x+1))
    for y in range(5,9):
        num = int(ID[y])
        total += (num * (y+1))
    return total % 10


def verify_check_digit(ID):
    if ID == '':
        return None, ''
    elif len(ID) != 10:
        return False, 'The length of the number given must be 10'
    elif ID[0:5].isalpha() == False:
        index = -1
        for char in ID[0:5]:
            index += 1
            if char.isalpha() == False:
                break
        return False, "The first 5 characters must be A-Z, the invalid character is at {} is {}".format(index, ID[index])
    elif ID[7:10].isdigit() == False:
        index = 6
        for char in ID[7:10]:
            index += 1
            if char.isdigit() == False:
                break
        return False, "The last 3 characters must be 0-9, the invalid character is at {} is {}".format(index, ID[index])
    elif not (ID[5] == '1' or ID[5] == '2' or ID[5] == '3'):
        return False, "The sixth character must be 1 2 or 3"
    elif not (ID[6] == '1' or ID[6] == '2' or ID[6] == '3' or ID[6] == '4'):
        return False, "The seventh character must be 1 2 3 or 4"
    elif get_check_digit(ID) != int(ID[9]):
        return False, "Check Digit {} does not match calculated value {}.".format(ID[9],get_check_digit(ID))
    else:
        return True, ''


if __name__ == "__main__":

    print("{:^70}".format('Linda Hall'))
    print("{:^70}".format('Library Card Check'))
    print('='*70)

    while True:
        
        ID = input("\nEnter Library Card. Hit Enter to Exit ==> ")

        boolean, condition = verify_check_digit(ID)

        if boolean == False:
            print('Library card is invalid.')
            print(condition)
        elif boolean == None:
            break
        elif boolean == True:
            print('Library card is valid.')
            print('The card belongs to a student in {}'.format(get_school(ID)))
            print('The card belongs to a {}'.format(get_grade(ID)))