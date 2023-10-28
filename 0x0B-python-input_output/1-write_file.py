#!/usr/bin/python3
""" defines a function that writes a string to a text file """


def write_file(filename="", text=""):
    """ writes a string to a text file and returns num of chars written """
    lines = 0
    words = 0
    characters = 0
    with open('filename', 'w') as file:
        file.write('text')
        for line in file:
            wordslist = line.split()
            lines = lines + 1
            words = words + len(wordslist)
            characters += sum(len(word) for word in wordslist)
        return characters
