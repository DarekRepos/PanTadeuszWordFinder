import os
import time
import click


@click.command()
@click.argument('words_input', type=click.File('r'))
@click.argument('searched_file', type=click.File('r'))
def calculate_words(words_input, searched_file):
    """ count specific word in "Pan Tadeusz" poem """

    # dir_path = os.path.dirname(__file__)
    # name = ["/words-list.txt", "/pan-tadeusz-czyli-ostatni-zajazd-na-litwie.txt"]

    # Open the list of words
    # for which we want to count the occurrence
    #  in the text of the book "Pan Tadeusz"
    file = words_input.readlines()

    word_list = [elt.strip() for elt in file]

    word_set = set(word_list)

    counter = 0
    word_counter = 0

    start_time = time.time()

    # calculate total number for lines and words
    for line in nonblank_lines(searched_file):
        counter += 1
        # each word is separated by space 
        for word in line.split(" "):
            if word in word_set:
                word_counter += 1

    stop_time = time.time()

    print("Number of lines : %d" % counter)
    print("Found: %d words" % word_counter)
    print("Time elapsed: %.1f second" % (stop_time - start_time))


def nonblank_lines(text_file):
    """[summary]
    
    Function to erase blank lines from text string

    Input: text with 

    Arguments:
    my_words {String} -- Given string from txt File

    Yields:
    String object -- Lines of text poem
    """
    for lines in text_file:
        line = lines.rstrip()
        if line:
            yield line

if __name__ == "__main__":
    calculate_words()