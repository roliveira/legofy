#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
"""

import os
import sys
import getopt

import legofy


def main():
    input = ''
    output = ''

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hi:o:',
                                   ['help', 'input=', 'output='])

    except getopt.GetoptError as err:
        print str(err)
        print '\n\t%s -i <input> -o <output>' % os.path.basename(sys.argv[0])
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print '%s -i <input> -o <output>' % os.path.basename(sys.argv[0])
            sys.exit()

        elif opt in ('-i', '--input'):
            input = arg

        elif opt in ('-o', '--output'):
            output = arg

    _ = legofy(input, fname=output)

if __name__ == "__main__":
    main()
