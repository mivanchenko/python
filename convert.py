#!/usr/bin/env python3

import sys

ord2utf = {
    207: '\u041F', # П
    224: '\u0430', # а
    225: '\u0431', # б
    226: '\u0432', # в
    227: '\u0433', # г
    228: '\u0434', # д
    229: '\u0435', # е
    230: '\u0436', # ж
    231: '\u0437', # з
    232: '\u0438', # и
    233: '\u0439', # й
    234: '\u043A', # к
    235: '\u043B', # л
    236: '\u043C', # м
    237: '\u043D', # н
    238: '\u043E', # о
    239: '\u043F', # п
    240: '\u0440', # р
    241: '\u0441', # с
    242: '\u0442', # т
    243: '\u0443', # у
    244: '\u0444', # ф
    245: '\u0445', # х
    246: '\u0446', # ц
    247: '\u0447', # ч
    248: '\u0448', # ш
    249: '\u0449', # щ
#    : '\u',
}

if len(sys.argv) < 2:
    print('Usage:', sys.argv[0], '[filename]')
    exit()

infile = sys.argv[1]

with open(infile) as f:
#    first_line = list(f)[0]
#    print(first_line, end='')
#    for letter in first_line:
#        utf = ord2utf.get(ord(letter), '')
#        print(utf, end='')
#    print()

    for line in list(f):
        for letter in line:
            utf = ord2utf.get(ord(letter), '')
            print(utf, end='')
        print()
f.close()

