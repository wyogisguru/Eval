#-------------------------------------------------------------------------------
# Name:        rightmost_char.py
# Purpose:     Given a string 'S' and a character 't' print out the rightmost
#              occurrence of 't' (case matters) in 'S' or -1 if there is none.
#              The position to be printed out is zero based.
#
# Author:      cbrink
#
# Created:     24/11/2015
# Copyright:   (c) cbrink 2015
#-------------------------------------------------------------------------------
import sys
import traceback
# ------------------------------------------------------------------------------
def letter_t(lines=None):
    try:
        # Create new list from 'lines' that has removed all blank strings...
        newLines = [string for string in lines if string != '\n']

        # Find what letter 't' is...
        for line in newLines:

            for char in line:
                if char == ',':
                    t = line.index(char) + 1
                    find_t(t, line)

    except Exception, err:
        print('print_exc():')
        traceback.print_exc(file=sys.stdout)
# ------------------------------------------------------------------------------
def find_t(t=None,
           string=None):
    try:
        S = string
        tIndexes = []
        for char in S:
            # Check for case of letter...
            if char.lower() == S[t].lower():
                print(char.lower(), ' = ', S[t].lower())
                # Create list of occurences of t....
                tIndexes.append(S.index(char))
            else:
                if char == ',':
                    break

        # Pass 't' occurrences list to print function...
        print_output(tIndexes)

    except Exception, err:
        print('print_exc():')
        traceback.print_exc(file=sys.stdout)
# ------------------------------------------------------------------------------
def print_output(t_occurence=None):
    try:
        # If no 't' was found print -1...
        if len(t_occurence) == 0:
            no_t = -1
            print(no_t)
        else:
            if len(t_occurence) >= 1:
                # Print right most occurence of 't' that is zero based...
                rm_t = t_occurence[-1]
                print(rm_t)

    except Exception, err:
        print('print_exc():')
        traceback.print_exc(file=sys.stdout)
#-------------------------------------------------------------------------------
def main():
    try:
        test_cases = open(sys.argv[1],
                          'r')

        lines = []
        for test in test_cases:
            lines.append(str(test))

        letter_t(lines)

        test_cases.close()
        sys.exit(0)

    except Exception, err:
        print('print_exc():')
        traceback.print_exc(file=sys.stdout)
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
