# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 09:51:24 2018

"""

def random_generator():
    import random
    from random import randint
    random_number = randint(0, 10000000000)
    computer_choice = 0
        ## Use the random number for computer to give 0 or 1 random numbers.
    if random_number <= 2**31:
        computer_choice = 0
    else:
        computer_choice = 1
    return computer_choice
