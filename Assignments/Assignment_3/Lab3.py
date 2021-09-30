'''
CS 101 Lab
Program #3
Levi Lindskog is my name in Canvas, but I go by Levi Estabrook.
lhl8r5@umsystem.edu

PROBLEM:
Program must be able to guess user's number between 1 and 100 inclusive.
Only user input will be of the user's number's remainder when divided by 3, 5, and 7.
After guessing correctly, program must ask user whether they wish to continue playing. 
Y or N are the only valid responses to this.
'''

#ALGORITHM

print('Welcome to the Flarsheim Guesser!\n')

playing = True
while playing == True:
    print('Please think of a number between and including 1 and 100.\n')

    valid3 = None
    while valid3 != True:
        div3 = int(input('What is the remainder when your number is divided by 3? '))
        if div3 < 0:
            print('The value entered must be 0 or greater')
        elif div3 > 2:
            print('The value entered must be less than 3')
        else:
            print()
            valid3 = True
    
    valid5 = None
    while valid5 != True:
        div5 = int(input('What is the remainder when your number is divided by 5? '))
        if div5 < 0:
            print('The value entered must be 0 or greater')
        elif div5 > 4:
            print('The value entered must be less than 5')
        else:
            print()
            valid5 = True
    
    valid7 = None
    while valid7 != True:
        div7 = int(input('What is the remainder when your number is divided by 7? '))
        if div7 < 0:
            print('The value entered must be 0 or greater')
        elif div7 > 6:
            print('The value entered must be less than 7')
        else:
            print()
            valid7 = True

    list1 = []
    for x in range(0,101):
        if x % 3 == div3:
            list1.append(x)

    list2 = []
    for y in list1:
        if y % 5 == div5:
            list2.append(y)

    for z in list2:
        if z % 7 == div7:
            user_number = z
            break
        else:
            user_number = None

    if user_number != None:
        print('Your number was', user_number)
        print('How amazing is that?\n')
    else:
        print('Your number wasn\'t between 1 and 100.\n')
    
    validplay = None
    while validplay == None:
        play_again = input('Do you want to play again? Y to continue, N to quit  ==> ')
        if play_again == ('n' or 'N'):
            validplay = True
            playing = False
        elif play_again == ('y' or 'Y'):
            validplay = True
            print()
    