#!/usr/bin/env python3
"""Create a dictionary of color names and their hex representations,
   and perform some operations on the dict.

Usage:

    python3 colors.py
"""

colors = dict(aquamarine='#7FFFD4', burlywood='#DEB887',
              chartreuse='#7FFF00', cornflower='#6495ED',
              firebrick='#B22222', honeydew='#F0FFF0',
              maroon='#B03060', sienna='#A0522D')

#Print out dictionary
for key in colors:
    print("{key} => {value}".format(key=key, value=colors[key]))
