#	CS-210 Project 3: Grocery Tracking Program
#	@file PythonCode.py
#	@author Eric Farkas
#	@version 1.2 8/14/22

import re
import string
import collections


def ItemCounter():
    # Open file (safely) and use the collections module to store the values as a dictionary
    with open('CS210_Project_Three_Input_File.txt') as fp:
        counts = collections.Counter(line.strip() for line in fp)
    for key in counts:
        print('%s %d' % (key, counts[key]))


def SpecificItemCounter(v):
    v = v.capitalize()
    # Open file to read and use the built-in count function
    with open('CS210_Project_Three_Input_File.txt') as fp:
        data = fp.read()
        occurences = data.count(v)
    return occurences


def ItemCounterWriter():
    # Open both the read and the write files
    with open('frequency.dat', "w") as wp:
        with open('CS210_Project_Three_Input_File.txt') as fp:
            counts = collections.Counter(line.strip() for line in fp)
            # Write the item and counts to the output file
            for key in counts:
                wp.write('%s %d\n' % (key, counts[key]))
            # If the file was properly closed, tell the user
            if wp.closed:
                print('Success')