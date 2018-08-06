#!/usr/bin/env python3

import sys

#letter = 'є'

if len(sys.argv) >= 2:
    for letter in sys.argv[1:]:
        print(letter + '\u0301')
