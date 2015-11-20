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
def read_file(file=None):
    txtFile = open(file,
                   'r')
    lines = txtFile.readlines()

    # Create new list from lines that has removed all blank line items...
    newLines = [string for string in lines if string != '\n']

    # Find value of 't'...
    for line in newLines:

        for char in line:
            if char == ',':
                t = line.index(char) + 1
                find_t_index(t, line)
# ------------------------------------------------------------------------------
def find_t_index(t=None,
                 string=None):
    for char in string:
        tIndexes = []
        if char == string[t]:
            tIndexes.append(string.index(char))
            tIndex = tIndexes[-1]
            print tIndex
        else:
            if char == ',':
                break
#-------------------------------------------------------------------------------
def main():
##    path = str(input('Please provide full path to text file:'))
##    if path.isdigit():
##        print('Input cannot be just a number!'
##              'Please run program again and input full path to text file!')
##    else:
##        read_file(path)

    path = r'C:\Temp\rightmost_char.txt'
    read_file(path)

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
