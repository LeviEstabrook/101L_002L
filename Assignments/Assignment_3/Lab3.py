'''
CS 101 Lab
Program #2
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

T_rem0 = []
T_rem1 = []
T_rem2 = []
for t in range(1,101):
    if t % 3 == 0:
        T_rem0.append(t)
    elif t % 3 == 1:
        T_rem1.append(t)
    elif t % 3 == 2:
        T_rem2.append(t)

F_rem0 = []
F_rem1 = []
F_rem2 = []
F_rem3 = []
F_rem4 = []
for f in range(1,101):
    if f % 5 == 0:
        F_rem0.append(f)
    elif f % 5 == 1:
        F_rem1.append(f)
    elif f % 5 == 2:
        F_rem2.append(f)
    elif f % 5 == 3:
        F_rem3.append(f)
    elif f % 5 == 4:
        F_rem4.append(f)

S_rem0 = []
S_rem1 = []
S_rem2 = []
S_rem3 = []
S_rem4 = []
S_rem5 = []
S_rem6 = []
for s in range(1,101):
    if s % 7 == 0:
        S_rem0.append(s)
    elif s % 7 == 1:
        S_rem1.append(s)
    elif s % 7 == 2:
        S_rem2.append(s)
    elif s % 7 == 3:
        S_rem3.append(s)
    elif s % 7 == 4:
        S_rem4.append(s)
    elif s % 7 == 5:
        S_rem5.append(s)
    elif s % 7 == 6:
        S_rem6.append(s)
'''
print(T_rem0)
print(T_rem1)
print(T_rem2)
print(F_rem0)
print(F_rem1)
print(F_rem2)
print(F_rem3)
print(F_rem4)
print(S_rem0)
print(S_rem1)
print(S_rem2)
print(S_rem3)
print(S_rem4)
print(S_rem5)
print(S_rem6)
'''


playing = True
while playing == True:
    print('Please think of a number between and including 1 and 100.\n')

    valid3 = None
    while valid3 != True:
        div3 = int(input('What is the remainder when your number is divided by 3 ?'))
        if div3 < 0:
            print('The value entered must be 0 or greater')
        elif div3 > 2:
            print('The value entered must be less than 3')
        else:
            valid3 = True
    
    valid5 = None
    while valid5 != True:
        div5 = int(input('What is the remainder when your number is divided by 5 ?'))
        if div5 < 0:
            print('The value entered must be 0 or greater')
        elif div5 > 4:
            print('The value entered must be less than 5')
        else:
            valid5 = True
    
    valid7 = None
    while valid7 != True:
        div7 = int(input('What is the remainder when your number is divided by 7 ?'))
        if div7 < 0:
            print('The value entered must be 0 or greater')
        elif div7 > 6:
            print('The value entered must be less than 7')
        else:
            valid7 = True

