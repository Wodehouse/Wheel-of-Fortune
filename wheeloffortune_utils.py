import string
import random

def choosePhrase():
    """
    Purpose: Chooses a random phrase from the file "wheeloffortune.txt"
    Parameters: None
    Return (list): a phrase as a list of characters, ex. ["l", "o", "l"]
    """
    phrases = open("wheeloffortune.txt")
    lines = phrases.readlines()
    idx = random.randrange(0,len(lines))
    return list(lines[idx].strip().lower())

def makePhraseString(phrase):
    """
    Purpose: Converts a list to a string 
    Parameters (list): a phrase as a list of characters, ex. ["l", "o", "l"]
    Return (str): a phrase as a string, e.g. "lol"
    """
    return "".join(phrase)

def spinWheel():
    """
    Purpose: Spin the wheel of fortune
    Parameters: None
    Return (int): a positive value (cash value) or -1 (bankruptcy).
    Side effects: None
    """
    wheel = [600, 700, 600, 650, 500, 700, -1, 
             600, 550, 500, 600, -1, 650, 700, 
             800, 500, 650, 500, 900, -1, 2500]
    spin = random.randrange(0, len(wheel))
    return wheel[spin]

