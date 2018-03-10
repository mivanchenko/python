#!/usr/bin/env python

class Point():
    pass

class Rectangle():
    pass

p1 = Point()
p1.x = 3.0
p1.y = 4.0

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

import copy

p2 = copy.copy(p1)

print(p1 == p2)
print(p1 is p2)

#print(box.width, box.height, box.corner.x, box.corner.y)

box2 = copy.copy(box)
#print(box2.width, box2.height, box2.corner.x, box2.corner.y)
print(box2 is box)
print(box2.corner is box.corner)

box3 = copy.deepcopy(box)
print(box3 is box)
print(box3.corner is box.corner)

print(type(p1))
print(type(box))

print(hasattr(p1, 'x'))
print(hasattr(p1, 'z'))

class Time():
    pass

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

def print_time(time):
    print('{:2d}:{:2d}:{:2d}'.format(time.hour, time.minute, time.second))

def repr_time(time):
    return '{:2d}:{:2d}:{:2d}'.format(time.hour, time.minute, time.second)

def is_after(time1, time2):
    return repr_time(time1) > repr_time(time2)

print_time(time)

time2 = Time()
time2.hour = 11
time2.minute = 59
time2.second = 29

print(is_after(time, time2))



