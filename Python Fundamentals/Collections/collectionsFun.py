#!/usr/bin/env python3
"""More experimentation with collection types, starting with Dicts.

Usage:

    python3 collectionsFun.py
"""
#Creating a basic dictionary of URLs.
urls = {'Google': 'http://google.com',
        'Pluralsight': 'http://pluralsight.com',
        'Sixty North': 'http://sixty-north.com',
        'Microsoft': 'http://microsoft.com'}

#Usage example. Should output 'http://pluralsight.com
urls['Pluralsight']

#Convert tuples into a dict
names_and_ages = [('Alice', 32), ('Bob', 48), ('Charlie', 28), ('Daniel', 33)]
d = dict(names_and_ages)
d        #Should output {'Alice': 32, 'Charlie': 28, 'Bob': 48, 'Daniel': 33}

#Another quick way to create a dict
phonetic = dict(a='alfa', b='baravo', c='charlie', d='delta', e='echo', f='foxtrot')
phonetic   #Should output the above in dict form.

#Two ways to copy a dict
#1:

d = dict(goldenrod=0xDAA520, indigo=0x4B0082, seashell=0xFFF5EEE)
e = d.copy()
e   #Should output the same thing as d.

#2:
f = dict(e)
f   #Should output the same thing as d and e.

#Merging two dicts.
g = dict(wheat=0xF5DEB3, khaki=0xF0E68C, crimson=0xDC143C)
f.update(g)
f   #Should output f and g together as one dict.

#Gotcha: values which are present in both dicts being merged will be overwritten.
stocks = {'GOOG': 891, 'AAPL': 416, 'IBM': 194}
stocks.update({'GOOG': 894, 'YHOO': 25})
stocks  #should output the two merged with the value 894 for GOOG.

#Dicts are iterable. Example:
colors = dict(aquarmarine='#7FFFD4', burlywood='#DEB887',
              chartreuse='#7FFF00', cornflower='#6945ED',
              firebrick='#B22222', honeydew='#F0FFF0',
              maroon='#B03060', sienna='#A0522D')

#Should iterate through dict Colors. Note that the order is inconsitent across runs.
for key in colors:
    print("{key} => {value}".format(key=key, value=colors[key]))

#printing only the values and not the keys.
for value in colors.values():
        print(value)

#Printing only the keys and not the values.
for key in colors.keys():
        print(key)

#Printing both the keys and the values as Tuples
for key, value in colors.items():
        print("{key} => {value}".format(key=key, value=value))

#testing for membership in dicts
symbols = dict(usd='\u0024', gbp='\u00a3', nzd='\u0024', krw='\u20a9',
               eur='\u20ac', jpy='\u00a5', nok='kr', ils='\u20aa', hhg='Pu')

#Should return true
'nzd' in symbols

#Should return false
'mkb' in symbols

#Deleting elements from a dict
z = {'H': 1, 'TC': 43, 'Xe': 54, 'Un': 137, 'Rf': 104, 'Fm': 100}
#Removes Unobtanium from the dict.
del z['Un']
z
