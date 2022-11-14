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


dir_path = os.path.dirname(__file__)
name = ["/words-list.txt", "/pan-tadeusz-czyli-ostatni-zajazd-na-litwie.txt"]

# Open the list of words
# for which we want to count the occurrence
#  in the text of the book "Pan Tadeusz"
file = open(dir_path + name[0], "r", encoding="utf-8").readlines()

word_list = [elt.strip() for elt in file]

word_set = set(word_list)

counter = 0
word_counter = 0

start_time = time.time()

# Open Pan Tadeusz book
with open(dir_path + name[1], "r", encoding="utf-8") as book_text:
    for line in nonblank_lines(book_text):
        counter += 1
        for word in line.split(" "):
            if word in word_set:
                word_counter += 1

stop_time = time.time()

print("Number of lines : %d" % counter)
print("Found: %d words" % word_counter)
print("Time elapsed: %.1f second" % (stop_time - start_time))
