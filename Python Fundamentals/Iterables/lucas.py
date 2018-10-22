"""
A module that generates the Lucas sequence of numbersself.

Usage: python3 lucas.py

"""

def lucas():
    """
    Generates the sequence starting with a hard-coded 2.
    """
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b

#This will run infinitely if looped. Example:
# for x in lucas():
#    print(x)
