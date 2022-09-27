"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    
    set_items = set(items)
    
    for i in set_items:
        frequencies[str(i)] = getFrequencyOf(i, items)

    
    return frequencies




def getFrequencyOf(letter, list):
    counter = 0
    letter = str(letter)
    for x in list:
        if str(x) == letter:
            counter+=1
    return counter



