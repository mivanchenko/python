#!/usr/bin/env python3

import sys

# taken from https://www.utf8-chartable.de/unicode-utf8-table.pl

if len(sys.argv) < 2:
    print('Usage:', sys.argv[0], '[filename]')
    exit()

ord2utf = {
    192: '\u0410', # А
    193: '\u0411', # Б
    194: '\u0412', # В
    195: '\u0413', # Г
    196: '\u0414', # Д
    197: '\u0415', # Е
    198: '\u0416', # Ж
    199: '\u0417', # З
    200: '\u0418', # И
    201: '\u0419', # Й
    202: '\u041A', # К
    203: '\u041B', # Л
    204: '\u041C', # М
    205: '\u041D', # Н
    206: '\u041E', # О
    207: '\u041F', # П
    208: '\u0420', # Р
    210: '\u0421', # С
    211: '\u0422', # Т
    212: '\u0423', # У
    213: '\u0424', # Ф
    214: '\u0425', # Х
    215: '\u0426', # Ц
    216: '\u0427', # Ч
    217: '\u0428', # Ш
    218: '\u0429', # Щ
    221: '\u042C', # Ь

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
    252: '\u044C', # ь
}

infile = sys.argv[1]

with open(infile) as f:
    # first_line = list(f)[0]
    # print(first_line, end='')
    # for letter in first_line:
    #     utf = ord2utf.get(ord(letter), '')
    #     print(utf, end=' ')
    #     utf = ord(letter)
    #     print(utf, end=' ')
    # print()

    with open('out.txt', 'w') as fout:
        for line in list(f):
            for letter in line:
                utf = ord2utf.get(ord(letter), letter)
                print(utf, end='')
                fout.write(utf)
    fout.close()
f.close()

