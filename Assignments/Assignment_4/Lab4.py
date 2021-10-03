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


def play_again():
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES. Keeps asking until they respond yes '''
    valid = None
    while valid == None:
        play = input('Do you want to play again? ==> ').lower()
        if play == 'y' or 'yes':
            return True
            valid = True
        elif play == 'n' or 'no':
            return False
            valid = True
        else:
            print('\nYou must enter Y/YES/N/NO to continue.  Please try again')



    return True
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''


    return 1            

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''


    return 1, 2, 3

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''


    return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''


    return 0

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''


    return wager * -1     


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()

        while True:  # Replace with condition for if they still have money.
            
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