'''
CS 101 Lab
Levi Lindskog is my name in Canvas, but I go by Levi Estabrook.
lhl8r5@umsystem.edu

PROBLEM:
Program must simulate a slot machine that has 3 reels, 
each reel having numbers ranging from 1 to 10.
The user can input how many chips they start out with.
The user must be able to wager between 1 and the amount of bank they currently have on each spin.
If the user matches 3 numbers from the slot machine, they will win 10 times their wager.
If the user matches 2 numbers, they will win 3 times their wager.
'''

#ALGORITHM

import math
import random

# take 1
def play_again():
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES. Keeps asking until they respond yes '''
    while True:
        play = input('Do you want to play again? ==> ').lower()
        if play == 'y' or 'yes':
            return True
        elif play == 'n' or 'no':
            return False
        else:
            print('\nYou must enter Y/YES/N/NO to continue.  Please try again')

# take 1
def get_wager(bank):
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    while True:
        wager = int(input('How many chips do you want to wager? ==> '))
        if wager <= 0:
            print('The wager amount must be greater than 0. Please enter again.')
        elif wager > bank:
            print('The wager amount cannot be greater than how much you have.', bank)
        else:
            return wager
            

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''


    return 1, 2, 3


def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''


    return 0

# take 1
def get_bank():
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    while True:
        bank = int(input('How many chips do you want to start with? ==> '))
        if bank <= 0:
            print('Too low a value, you can only choose 1 - 100 chips')
            continue
        elif bank > 100:
            print('Too high a value, you can only choose 1 - 100 chips')
            continue
        else:
            return bank


# take 1
def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        return wager*10
    elif matches == 2:
        return wager*3
    else:
        return -wager     


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while bank > 0:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()




'''
ERROR HANDLING:

'''