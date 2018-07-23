#!/usr/bin/env python3

def double(x):
    return x * 2

print(double(5))

triple = lambda x: x * 3

print(triple(5))

print((lambda x: x * 4)(5))

print((lambda x, y: x * y)(5, 5))
