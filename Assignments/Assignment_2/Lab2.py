'''
CS 101 Lab
Program #2
Levi Lindskog is my name in Canvas, but I go by Levi Estabrook
lhl8r5@umsystem.edu

PROBLEM:
Calculate CS101 Lab grades based off the weighting system.
The 3 categories and their weights are Labs:0.7, Lab_Exams:0.2, and Attendance:0.1.
Take inputs of student_name, lab_grade, exam_grade, and attendance_grade.
Output weighted_grade and letter_grade.
'''

#ALGORITHM

print('**** Welcome to the LAB grade calculator! ****\n')

student_name = input('Who are we calculating grades for? ==> ')
print()

lab_grade = int(input('Enter the Labs grade? ==> '))
if 0 > lab_grade:
    print('The lab value should have been zero or greater. It has been changed to zero.\n')
    lab_grade = 0
elif 100 < lab_grade:
    print('The lab value should have been 100 or less. It has been changed to 100.\n')
    lab_grade = 100
else:
    print()

exam_grade = int(input('Enter the EXAMS grade? ==> '))
if 0 > exam_grade:
    print('The exam value should have been zero or greater. It has been changed to zero.\n')
    exam_grade = 0
elif 100 < exam_grade:
    print('The exam value should have been 100 or less. It has been changed to 100.\n')
    exam_grade = 100
else:
    print()

attendance_grade = int(input('Enter the Attendance grade? ==> '))
if 0 > attendance_grade:
    print('The exam value should have been zero or greater. It has been changed to zero.\n')
    attendance_grade = 0
elif 100 < attendance_grade:
    print('The exam value should have been 100 or less. It has been changed to 100.\n')
    attendance_grade = 100
else:
    print()

weighted_grade = (0.7 * lab_grade) + (0.2 * exam_grade) + (0.1 * attendance_grade)
if 90 <= weighted_grade <= 100:
    letter_grade = 'A'
elif 80 <= weighted_grade < 90:
    letter_grade = 'B'
elif 70 <= weighted_grade < 80:
    letter_grade = 'C'
elif 60 <= weighted_grade < 70:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print('The weight grade for {} is {:.1f}'.format(student_name,weighted_grade))
print('{} has a letter grade of {}'.format(student_name, letter_grade))

print('\n**** Thanks for using the Lab grade calculator ****')

'''
ERROR HANDLING:
To avoid errors in calculation, integers that aren't within [0,100] are rounded to the nearest valid integer.
'''