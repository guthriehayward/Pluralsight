#!/usr/bin/env python3
"""
Some basic expirimentation with generators.

Usage:

    python3 generator.py
"""

#Creates a new generator which generates 1, 2, and 3.
def gen123():
    yield 1
    yield 2
    yield 3

#assigns gen123 to variable g.
g = gen123()

next(g)
#Returns 1
next(g)
#Returns 2
next(g)
#Returns 3
next(g)
#StopIteration exception

for v in gen123():
    print(v)

#Should print 1, 2, 3 seperated by new lines

#note that each generator is a new object.
h = gen123()
i = gen123()

next(h)
next(h)
next(i)

#should print 1, 2, 1 separated by new lines

#Another generator, tracing yield with print statements
def gen246():
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to yield 6")
    yield 6
