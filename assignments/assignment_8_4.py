"""Module for assignment 8.4."""

# 8.4 Open the file romeo.txt and read it line by line.
# For each line, split the line into a list of words
# using the split() method.
# The program should build a list of words.
# For each word on each line check to see if the word is already
# in the list and if not append it to the list.
# When the program completes, sort and print the resulting words
# in python sort() order as shown in the desired output.
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

file_name = input('Enter a file name: ')
try:
    file_handle = open(file_name)
except:
    print('Failed to open file',file_name)
    quit()

unique_words = list()
for line in file_handle:
    words = line.rstrip().split()
    for word in words:
        word_found = False
        for unique_word in unique_words:
            if word.upper() == unique_word.upper():
                word_found = True
                break
        if not word_found:
            unique_words.append(word)

unique_words.sort()
print(unique_words)