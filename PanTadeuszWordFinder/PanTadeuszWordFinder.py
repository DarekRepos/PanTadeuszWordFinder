import os

def nonblank_lines(my_words):
    for lines in my_words:    
        line = lines.rstrip()
        if line:
            yield line

dir_path = os.path.dirname(__file__)

word_list = [elt.strip() for elt in open(dir_path + "\words-list.txt","r").readlines()]
word_set = set(word_list)

counter = 0

with open(dir_path + "\pan-tadeusz-czyli-ostatni-zajazd-na-litwie.txt","r") as epics_words:
    for word in nonblank_lines(epics_words):
        if word not in word_set:
            print (word)
            counter += 1

print("Number of lines : %d" % counter)

