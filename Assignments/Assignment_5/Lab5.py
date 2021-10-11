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

ALGORITHM:
    1. Start
    2. Declare variables ID, boolean, condition.
    3. Read variable ID
    4. 
    69. Stop


Step 1: Start
Step 2: Declare variables n, i, flag.
Step 3: Initialize variables
        flag ← 1
        i ← 2  
Step 4: Read n from the user.
Step 5: Repeat the steps until i=(n/2)
     5.1 If remainder of n÷i equals 0
            flag ← 0
            Go to step 6
     5.2 i ← i+1
Step 6: If flag = 0
           Display n is not prime
        else
           Display n is prime
Step 7: Stop 




ERROR HANDLING:

'''


def get_school(ID):
    return 'Deez nuts'


def get_grade(ID):
    return 'FIXME'


def character_value(ID):
    return 'FIXME'


def get_check_digit(ID):
    return 'FIXME'


def verify_check_digit(ID):
    if ID == '':
        return None, ''
    elif len(ID) != 10:
        return False, 'The length of the number given must be 10'
    else:
        return False, 'FIXME'


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
            print('Go Go Gadget Commit Voter Fraud')


        print('NoInah')