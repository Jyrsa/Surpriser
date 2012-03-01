#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Inquisition.py contains functions surprise and surprise_file

Author jsuvileh
"""

import random
import time

SURPRISE_TEXT = "Nobody expects the %s inquisition!"

SURPRISE_ADJECTIVES = [
                "Spanish",
                "Härmäish",
                "spammish",
                "fish"
                ]

SURPRISE_MAX_SLEEP_TIME = 5 # sleep takes seconds

def surprise():
    """
        sleeps for a while, then
        prints a surprise method to stdout.
    """ 
    time.sleep(random.randrange(0, SURPRISE_MAX_SLEEP_TIME))
    print SURPRISE_TEXT % random.choice(SURPRISE_ADJECTIVES)

def surprise_file(filename):
    """ 
        sleeps for a while, then appends 
        a surprise message to a file
        named filename
    """
    time.sleep(random.randrange(0, SURPRISE_MAX_SLEEP_TIME))
    with open(filename, "a") as f:
        f.write(SURPRISE_TEXT % random.choice(SURPRISE_ADJECTIVES))
        f.write("\n") #write doesn't append an \n

