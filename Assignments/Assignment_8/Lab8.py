'''
CS 101 Lab
Program 8
Levi Lindskog is my name in Canvas, but I go by Levi Estabrook.
lhl8r5@umsystem.edu

PROBLEM:
Program must let user choose from a menu whether they want to:
Add a Test or Assignment score
Remove a Test or Assignment score
Clear all Test or Assignment scores
Calculate and display the min, max, mean, and std for list of Tests and Assignments
Quit.

ERROR HANDLING:


'''

#ALGORITHM

'''
Grade Menu
1 - Add Test
2 - Remove Test
3 - Clear Tests
4 - Add Assignment
5 - Remove Assignment
6 - Clear Assignments
D - Display Scores
Q - Quit

==> d

Type               #       min       max       avg       std
============================================================
Tests              0       n/a       n/a       n/a       n/a
Programs           0       n/a       n/a       n/a       n/a

The weighted scores is       0.00

'''

def menu_select():
    print(
        '\n            Grade Menu\n'
        '1 - Add Test\n'
        '2 - Remove Test\n'
        '3 - Clear Tests\n'
        '4 - Add Assignment\n'
        '5 - Remove Assignment\n'
        '6 - Clear Assignments\n'
        'D - Display Scores\n'
        'Q - Quit\n')
    select = None
    while select not in options:
        select = input('==> ').upper().strip()
    print()
    return select

def mean(scores_list):
    total = 0
    for score in scores_list:
        total+=score
    return total / len(scores_list)

def std(scores_list,mean):
    total = 0
    for score in scores_list:
        total += ((score - mean)**2)
    standard_deviation = (total/len(scores_list))**(1/2)
    return standard_deviation

def display():
    if len(test_scores_list) == 0:
        Tests = [0,'n/a','n/a','n/a','n/a']
    else:
        test_mean = mean(test_scores_list)
        test_std = std(test_scores_list,test_mean)
        Tests = [
            len(test_scores_list),
            min(test_scores_list),
            max(test_scores_list),
            test_mean,
            test_std]
    
    if len(assignment_scores_list) == 0:
        Programs = [0,'n/a','n/a','n/a','n/a']
    else:
        prgm_mean = mean(assignment_scores_list)
        prgm_std = std(assignment_scores_list,prgm_mean)
        Programs = [
            len(assignment_scores_list),
            min(assignment_scores_list),
            max(assignment_scores_list),
            prgm_mean,
            prgm_std]
    
    wmt = Tests[3]
    if wmt == 'n/a':
        wmt = 0
    wmp = Programs[3]
    if wmp == 'n/a':
        wmp = 0
    weighted = (wmt*.6) + (wmp*.4)

    print('Type               #       min       max       avg       std')
    print('='*60)
    if Tests[0] > 0:
        print('Tests{:>15d}{:>10.1f}{:>10.1f}{:>10.2f}{:>10.2f}'.format(Tests[0],Tests[1],Tests[2],Tests[3],Tests[4]))
    else:
        print('Tests{:>15d}{:>10s}{:>10s}{:>10s}{:>10s}'.format(Tests[0],Tests[1],Tests[2],Tests[3],Tests[4]))
    if Programs[0] > 0:
        print('Programs{:>12d}{:>10.1f}{:>10.1f}{:>10.2f}{:>10.2f}'.format(Programs[0],Programs[1],Programs[2],Programs[3],Programs[4]))
    else:
        print('Programs{:>12d}{:>10s}{:>10s}{:>10s}{:>10s}'.format(Programs[0],Programs[1],Programs[2],Programs[3],Programs[4]))
    print('\nThe weighted scores is       {:.2f}'.format(weighted))

def add_score(selection):
    global test_scores_list, assignment_scores_list
    if selection == '1':
        type = 'Test'
    else:
        type = 'Assignment'
    while True:
        try:
            score = float(input('Enter the new {} score 0-100 ==> '.format(type)))
            if score >= 0:
                if selection == '1':
                    test_scores_list.append(score)
                else:
                    assignment_scores_list.append(score)
                return
        except ValueError:
            continue

def remove_score(selection):
    global test_scores_list, assignment_scores_list
    if selection == '2':
        type = 'Test'
    else:
        type = 'Assignment'
    flag = 0
    while True:
        try:
            score = float(input('Enter the {} to remove 0-100 ==> '.format(type)))
            if selection == '2':
                if score in test_scores_list:
                    test_scores_list.remove(score)
                    flag+=1
            elif selection == '5':
                if score in assignment_scores_list:
                    assignment_scores_list.remove(score)
                    flag+=1
            elif flag == 0:
                print('Could not find that score to remove')
            return
        except ValueError:
            continue

def clear_scores(selection):
    global test_scores_list, assignment_scores_list
    if selection == '3':
        test_scores_list = []
    else:
        assignment_scores_list = []


options = ['1','2','3','4','5','6','D','Q']

test_scores_list = []
assignment_scores_list = []

while True:
    user_selection = menu_select()

    if user_selection == '1' or user_selection == '4':
        add_score(user_selection)
    elif user_selection == '2' or user_selection == '5':
        remove_score(user_selection)
    elif user_selection == '3' or user_selection == '6':
        clear_scores(user_selection)
    elif user_selection == 'D':
        display()
    else:
        break