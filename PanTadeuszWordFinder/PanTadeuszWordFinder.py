# -*- coding: utf-8 -*-
import os

def nonblank_lines(my_words):
    for lines in my_words:    
        line = lines.rstrip()
        if line:
            yield line

DIR_PATH = os.path.dirname(__file__)

WORD_LIST = [elt.strip() for elt in open(DIR_PATH + "\words-list.txt", "r").readlines()]
WORD_SET = set(WORD_LIST)

COUNTER = 0

with open(DIR_PATH + "\pan-tadeusz-czyli-ostatni-zajazd-na-litwie.txt", "r") as epics_words:
    for word in nonblank_lines(epics_words):
        if word not in WORD_SET:
            print(word)
            COUNTER += 1

print("Number of lines : %d" % COUNTER)
