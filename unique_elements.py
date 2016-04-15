#-------------------------------------------------------------------------------
# Name:        unique_elements
# Purpose:
#
# Author:      cbrink
#
# Created:     4/15/2016
# Copyright:   (c) cbrink 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys
import time
# ------------------------------------------------------------------------------
def main():
##    test_cases = open(
##        sys.argv[1], 'r'
##        )

    txtFile = r'C:\Users\cbrink\Desktop\test.txt'

    with open(txtFile) as test_cases:
        numbers = []
        for line in test_cases:
            if line.isdigit():
                numbers.append(line)

        print(numbers)

##        numbers = [string for string in numbers if string != '\n']
##
##        print(numbers)

    time.sleep(5)

    sys.exit(0)
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
