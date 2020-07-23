"""
Header comment
"""
from wheeloffortune_utils import *
"""
Wheel of Fortune game
how to go to the next line so that my code is not beyond the line
"""

from wheeloffortune_utils import *

letter_list = "qwertyuiopasdfghjklzxcvbnm"

def initPuzzle(answer):
    """function that takes a list and returns a coded list"""
    puzzle=[]
    for i in range(len(answer)):
        if answer[i] in letter_list:
            member = "*"
        elif answer[i] == " ":
            member = "_"
        else:
            member = answer[i]
        puzzle.append(member)
    return puzzle

def updatePuzzle(puzzle, letter, answer):
    """function that updates a puzzle if a letter chosen is in the answer"""

    for i in range(len(answer)):
        if answer[i] == letter:
            puzzle[i] = letter     #lists are mutable

def askForLetter(command,letter_list):
    """asks for a letter within the given options"""
    condition = True       #set to keep the loop going
    while condition:
        choice = input("%s" %(command))
        if choice not in letter_list:
            print("%s is not valid. Please try again. " %(choice))

        else:
            condition = False
    return choice

def menu(opts):
    """function that writes a menu from a given list and records the user's choice as an integer in a given range"""
    length = len(opts)
    print("Choose the search criteria:")
    for i in range(length):                 #writes out the menu
        print("%d. %s" %(i+1, opts[i]))
    condition = True       #set to keep the loop going since it is hard to write out a condition

    while condition:
        choice = input("Your choice: ")
        digit = choice.isdigit()
        if digit:
            choice = int(choice)
            if choice not in range(1, len(opts)+1):           #Integer not in the given range
                print("Please enter an integer within the  given range!! ")
            else:
                condition = False             #to get out of the loop
        elif digit == False:
            print("Please a valid integer!! ")

    return choice

def alldigits(char):
    """function that checks if a string is made up entirely of digits"""
    int_list = "1234567890"
    count = 0
    for i in range(len(char)):
        if char[i] not in int_list:
            return False
    return True

def doSpinWheel(money, puzzle, answer):
    """function that spins the wheel and acts on the outcomes"""
    outcome = spinWheel()
    if outcome > 0:
        print("The wheel spins and lands on $ %d" %(outcome))
        guess = askForLetter("Enter a letter:"\
        "", letter_list)
        occur = answer.count(guess)
        occur_puz = puzzle.count(guess)
        updatePuzzle(puzzle, guess, answer)
        if occur > 0 and occur_puz == 0:
            extra = occur*outcome
            print("There are %d of %s in the phrase. You win %d!"\
             %(occur, guess, extra))
            money = money + extra
        elif occur > 0 and occur_puz != 0:
            print("You already chose %s!" %(guess))
        else:
            print("Oh no! There is no %s in the phrase!" %(guess))
    else:
        print("The wheel spins and lands on BANKRUPT!")
        money = 0
    return money

def doGuessPuzzle(answer):
    """checks if the player's guess is correct"""
    player_guess = input("What is your guess? ")
    if player_guess == makePhraseString(answer):
        return True
    else:
        return False

def main():

    answer = choosePhrase()
    print("Welcome to WHEEL OF FORTUNE!")
    puzzle = initPuzzle(answer)# call initPuzzle
    money = 0
    num_turns = 0
    condition = True
    while condition:
        print("Puzzle: %s" %(makePhraseString(puzzle)))
        print("You have $ %d. What do you want to do?" %(money))
        options = ["Spin the Wheel. ", "Guess the phrase. ", "Quit. (No Fun!)"]
        choice = menu(options)
        if choice == 1:
            money = doSpinWheel(money, puzzle, answer)
        elif choice == 2:
            player_guess = doGuessPuzzle(answer)
            if player_guess:
                print("You are right! Congratulations!\nYou solved the puzzle"\
                " after %d turns and with $ %d \nThanks for playing.\nAnswer "\
                "is '%s'" %(num_turns, money, makePhraseString(answer)))
                condition = False
            else:
                print("Nice attempt. You'll have to try again though.\n")
        else:
            print("Quitting...\nYou gave up after %d turns. Thanks for "\
            "playing.\nAnswer is '%s'" %(num_turns,makePhraseString(answer)))
            condition = False
        print("-"*50)
        num_turns = num_turns + 1

main()
