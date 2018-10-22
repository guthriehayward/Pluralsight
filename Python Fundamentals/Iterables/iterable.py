#!/usr/bin/env python3
"""
Returns the first iteration of an iterable. Handles the StopIteration exception.
Usage:

    python3 iterable.py
"""
def first(iterable):
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueEror("iterable is empty")
