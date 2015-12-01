#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      cbrink
#
# Created:     01/12/2015
# Copyright:   (c) cbrink 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import sys

def main():
    test_cases = open(sys.argv[1],
                      'r')
    numbers = []
    for num in test_cases:
        numbers.append(int(num))

    print(sum(numbers))

    sys.exit(0)

if __name__ == '__main__':
    main()
