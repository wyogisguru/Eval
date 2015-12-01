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
    for oddNum in range(1, 100, 2):
        print(oddNum)

    sys.exit(0)

if __name__ == '__main__':
    main()
