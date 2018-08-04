#!/usr/bin/env python3

messages = ['mess1', 'mess2', 'mess3']
messages = ''

#for message in messages:
#    print(message)

mess = messages or 'hey'
#print(mess)

import secrets

sec = secrets.randbits(8)
#print(sec)

from datetime import datetime

#print(datetime.utcnow())

li = [1, 2, 3]
li = []
#if li:
#    print('li')

import unittest

a_str = 'abc' 'def' 'ghi'
#print(a_str)

class StrCase(unittest.TestCase):
    def test_str(self):
        self.assertEqual(a_str, 'abcdefghi')

#if __name__ == '__main__':
#    unittest.main(verbosity=2)

#code = 0e0
#
#if code:
#    print('ok')

code: int = 4
label: str = '<unknown>'
#print(code)

import re

#matches = re.findall(r'\w+', 'abc abc')
#print(matches)
#matches = re.sub(r'(\w+) \1', r'\1', 'abc abc')
#print(matches)
