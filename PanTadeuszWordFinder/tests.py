import os
import subprocess
import sys

from PanTadeuszWordFinder.PanTadeuszWordFinder import calculate_words, nonblank_lines

# Functional test

def test_help():
    exit_status = os.system('python3 PanTadeuszWordFinder.py --help')
    assert exit_status == 0
    
def test_valid_files():
    exit_status = os.system('python3 PanTadeuszWordFinder.py words-list.txt pan-tadeusz-czyli-ostatni-zajazd-na-litwie.txt')
    assert exit_status == 0

def test_too_low_arguments():
    exit_status = subprocess.run(['python3','PanTadeuszWordFinder.py', 'words-list.txt'], capture_output=True, text=True)
    assert True == exit_status.stderr.__contains__('Error: Missing argument')

def test_not_existed_file():
    exit_status = subprocess.run(['python3','PanTadeuszWordFinder.py', 'words-list.txt', 'nonexisted_file.txt'], capture_output=True, text=True)
    assert True == exit_status.stderr.__contains__(' No such file or directory')

def test_number_of_lines():
    result = subprocess.run(['python3','PanTadeuszWordFinder.py', 'words-list.txt', 'pan-tadeusz-czyli-ostatni-zajazd-na-litwie.txt'], capture_output=True, text=True)
    assert True == result.stdout.__contains__('Number of lines : 9955')

def test_number_of_words():
    result = subprocess.run(['python3','PanTadeuszWordFinder.py', 'words-list.txt', 'pan-tadeusz-czyli-ostatni-zajazd-na-litwie.txt'], capture_output=True, text=True)
    assert True == result.stdout.__contains__('Found: 135 words')

def test_time_in_second():
    result = subprocess.run(['python3','PanTadeuszWordFinder.py', 'words-list.txt', 'pan-tadeusz-czyli-ostatni-zajazd-na-litwie.txt'], capture_output=True, text=True)
    assert True == result.stdout.__contains__('Time elapsed: 0.0')
    
    # Unit tests

    # test nonblank_lines function

def test_nonblank_lines():
   pass