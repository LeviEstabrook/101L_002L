'''
CS 101 Lab
Program 7
Levi Lindskog is my name in Canvas, but I go by Levi Estabrook.
lhl8r5@umsystem.edu

PROBLEM:
Program must be able to read through file containing information about fuel economy
and output the results to a file above a threshold that the user gives.
Program must ask user for a minimum fuel economy
and be able to handle non float data being entered.
Program must continually ask for a correct value greater than 0 and less than 100.
Program must ask for an input file and should loop until the user gives a valid file,
and the Program must do the same for an output file.
Program must be able to handle errors from incorrect values that may arise.

ERROR HANDLING:
Was encountering the FileNotFoundError with vehicles2.txt in the Assignment_7 folder alongside Lab7.py.
Fixed Error by moving txt files to sit only in the 101L_002L folder.
That was very confusing, I would have liked it of we had gone over that during the Monday Meeting.

'''

#ALGORITHM

def get_mpg():
    while True:
        try:
            mpg = float(input('Enter the minimum mpg ==> '))
            if mpg<=0:
                print('Fuel economy given must be greater than 0')
            elif mpg>100:
                print('Fuel economy must be less than 100')
            else:
                print()
                return mpg
        except ValueError:
            print('You must enter a number for the fuel economy')

def open_file(message, mode='r'):
    while True:
        try:
            user_input = input(message)
            if mode == 'w':
                try:
                    test = open(user_input, "r")
                    test.close()
                except IOError:
                    print('There is an IO Error',user_input)
                    continue
            file = open(user_input, mode)
            print()
            return file
        except FileNotFoundError:
            print('Could not open file',user_input)


mpg = get_mpg()

input_file = open_file('Enter the name of the input vehicle file ==> ')
input_file.readline()

output_file = open_file('Enter the name of the file to output to ==> ','w')
for car in input_file:
    attributes = car.split('\t')
    try:
        combinedmpg = float(attributes[-3])
        if combinedmpg >= mpg:
            print('{:<5}{:<20}{:<40}{:>10.3f}'.format(attributes[0],attributes[1],attributes[2],combinedmpg), file=output_file)
    except ValueError:
        print('Could not convert value {} for vehicle {} {} {}'.format(attributes[-3],attributes[0],attributes[1],attributes[2]))

input_file.close()
output_file.close()