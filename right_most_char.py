#-------------------------------------------------------------------------------
# Name:        rightmost_char.py
# Purpose:     Given a string 'S' and a character 't' print out the rightmost
#              occurrence of 't' (case matters) in 'S' or -1 if there is none.
#              The position to be printed out is zero based.
#
# Author:      cbrink
#
# Created:     20/11/2015
# Copyright:   (c) cbrink 2015
#-------------------------------------------------------------------------------
import time
# ------------------------------------------------------------------------------
def read_file(file=None):
    txtFile = open(file,
                   'r')
    lines = txtFile.readlines()

    # Create new list from 'lines' that has removed all blank strings...
    newLines = [string for string in lines if string != '\n']

    # Find what letter 't' is...
    for line in newLines:

        for char in line:
            if char == ',':
                t = line.index(char) + 1
                find_t(t, line)
# ------------------------------------------------------------------------------
def find_t(t=None,
           string=None):
    S = string
    tIndexes = []
    for char in S:
        if char == S[t]:
            # Create list of occurences of t....
            tIndexes.append(S.index(char))
        else:
            if char == ',':
                break

    # Pass 't' occurrences list to print function...
    print_output(tIndexes)
# ------------------------------------------------------------------------------
def print_output(t_occurence=None):
    # If no 't' was found print -1...
    if len(t_occurence) == 0:
        no_t = -1
        print(no_t)
    else:
        if len(t_occurence) >= 1:
            # Print right most occurence of 't' that is zero based...
            rm_t = t_occurence[-1]
            print(rm_t)

    # Allow users to see printed output for 5 seconds...
    time.sleep(5)
#-------------------------------------------------------------------------------
def main():
    filePath = str(input("Input file path including quotes: "
                         "(i.e.'C:\Temp\your_text_file.txt')"))

    if filePath.isdigit():
        print('Input cannot be just a number! '
              '(Please run program again and input full path to text file.)')
        time.sleep(5)
    else:
        read_file(filePath)
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
