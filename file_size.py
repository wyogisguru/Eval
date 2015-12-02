#-------------------------------------------------------------------------------
# Name:        file_size.py
# Purpose:     Read in a file and report its file size in bytes.
#
# Author:      cbrink
#
# Created:     02/12/2015
# Copyright:   (c) cbrink 2015
#-------------------------------------------------------------------------------
import sys
import os
import traceback
# ------------------------------------------------------------------------------
def main():
    try:
        test_cases = open(sys.argv[1],
                          'r')

        test_cases.seek(0, 2)

        print(test_cases.tell())

        sys.exit(0)

    except Exception, err:
        print('print_exc():')
        traceback.print_exc(file=sys.stdout)
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    main()
