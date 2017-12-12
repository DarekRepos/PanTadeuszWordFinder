my_words = [elt.strip() for elt in open("E:\Programy Python\PanTadeuszWordFinder\PanTadeuszWordFinder\pan-tadeusz-czyli-ostatni-zajazd-na-litwie.txt","r").readlines()]
word_list = [elt.strip() for elt in open("E:\Programy Python\PanTadeuszWordFinder\PanTadeuszWordFinder\words-list.txt","r").readlines()]

counter = 0

for word in my_words:
    if word not in word_list:
        print(word)
        counter += 1

print("Number of lines : %d" % counter)