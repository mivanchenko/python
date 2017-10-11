#my_unicode = "Привіт"
#my_unicode = "Hello"
#my_unicode = b"Hello"
#print(type(my_unicode))

#print("\N{GREEK CAPITAL LETTER DELTA}")
#print("\N{Latin Capital Letter Ezh}")
#print("\u01b7")
#print("\U000001b7")
#print(chr(439))
#print(ord("\N{Latin Capital Letter Ezh}"))

# The opposite method of bytes.decode() is str.encode()

#!/usr/bin/env python
# -*- coding: latin-1 -*-

import re
p = re.compile('\d+', re.ASCII)
s = "Over \u0e55\u0e57 57 flavours"
m = p.search(s)
#print(repr(m.group()))
#print(m.group())
