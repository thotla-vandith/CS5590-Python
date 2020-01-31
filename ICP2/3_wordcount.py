#Program to count the number of words in a text file

from collections import *
def word_count(file_name):
    with open(file_name) as f:
        return Counter(f.read().split())
print("Number of words in the given file is/are: ",word_count("sample.txt"))