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

import random

# take 2
def play_again():
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES. Keeps asking until they respond yes '''
    while True:
        play = input('Do you want to play again? ==> ').lower()
        if (play == 'y') or (play == 'yes'):
            return True
        elif (play == 'n') or (play == 'no'):
            return False
        else:
            print('\nYou must enter Y/YES/N/NO to continue.  Please try again')

# take 1
def get_wager(bank):
    ''' Asks the user for a wager chip amount. Continues to ask if they result is <= 0 or greater than the amount they have '''
    while True:
        wager = int(input('How many chips do you want to wager? ==> '))
        if wager <= 0:
            print('The wager amount must be greater than 0. Please enter again.')
        elif wager > bank:
            print('The wager amount cannot be greater than how much you have.', bank)
        else:
            return wager

# take 1
def get_slot_results():
    ''' Returns the result of the slot pull '''
    first = random.randint(1,10)
    second = random.randint(1,10)
    third = random.randint(1,10)
    return first, second, third

# take 1
def get_matches(reela, reelb, reelc):
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if (reela == reelb) and (reela == reelc):
        return 3
    elif ((reela == reelb) or (reela == reelc)) or (reelb == reelc):
        return 2
    else:
        return 0

# take 1
def get_bank():
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    while True:
        bank = int(input('How many chips do you want to start with? ==> '))
        if bank <= 0:
            print('Too low a value, you can only choose 1 - 100 chips')
        elif bank > 100:
            print('Too high a value, you can only choose 1 - 100 chips')
        else:
            return bank

# take 2
def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        return wager*9
    elif matches == 2:
        return wager*2
    else:
        return -wager     


if __name__ == "__main__":

    playing = True
    while playing:

        spins = 0
        bank = get_bank()
        start_money = bank
        max = start_money
        while bank > 0:

            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            spins += 1
            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            if bank > max:
                max = bank

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()

        print("You lost all", start_money, "in", spins, "spins")
        print("The most chips you had was", max)
        playing = play_again()




'''
ERROR HANDLING:
On payout, user receives either 3 times their wager or 10, depending on whether they rolled 2 matches or 3.
The initial wager is included as a part of this payout, meaning in calculation the program was
incorrectly letting the user win their wager back plus 3 or 10 times it.
This logic error was handled by tweaking the get_payout function to multiply the wager by 2 or 9, instead of 3 or 10 respectively.
The end result during payout is the bank retaining the wager initially bet, and additionally gaining 2 or 9 times the wager.
There was no logic error found when calculating payout upon rolling 0 matches.
'''