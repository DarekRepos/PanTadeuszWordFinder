"""
Count specific word in "Pan Tadeusz" poem
"""
# -*- coding: utf-8 -*-
import os

def nonblank_lines(my_words):
    """[summary]

    Function to erase blank lines from text string

    Arguments:
    my_words {[type]} -- [description]

    Yields:
    [type] -- [description]
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

with open(DIR_PATH + NAME[1], "r", encoding="utf-8") as epics_words:
    for word in nonblank_lines(epics_words):
        if word not in WORD_SET:
            print(word)
            COUNTER += 1

print("Number of lines : %d" % COUNTER)
