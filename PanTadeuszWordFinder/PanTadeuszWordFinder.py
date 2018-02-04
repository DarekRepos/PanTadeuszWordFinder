"""
count specific word in "Pan Tadeusz" poem
"""
# -*- coding: utf-8 -*-
import os
import time

def nonblank_lines(my_words):
    """[summary]

    Function to erase blank lines from text string

    Arguments:
    my_words {String} -- Given string from txt File

    Yields:
    String object -- Lines of text poem
    """
    for lines in my_words:
        line = lines.rstrip()
        if line:
            yield line

DIR_PATH = os.path.dirname(__file__)
NAME = ["\\words-list.txt", "\\pan-tadeusz-czyli-ostatni-zajazd-na-litwie.txt"]

WORD_LIST = [elt.strip() for elt in open(DIR_PATH + NAME[0], "r", encoding="utf-8").readlines()]
WORD_SET = set(WORD_LIST)

COUNTER = 0
WORD_COUNTER = 0
START = time.time()

with open(DIR_PATH + NAME[1], "r", encoding="utf-8") as epics_words:
    for mix_words_in_line in nonblank_lines(epics_words):
        print(mix_words_in_line)
        COUNTER += 1 
        for word in mix_words_in_line.split(" "):                   
            if word in WORD_SET:
                WORD_COUNTER += 1

STOP = time.time()

# TODO: word is sentence and saparate words
print("Number of lines : %d" % COUNTER)
print("Found: %d words"% WORD_COUNTER)
print("Time elapsed: %.1f second" % (STOP - START))
