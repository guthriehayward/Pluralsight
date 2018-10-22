#!/usr/bin/env python3
"""
Checks if a number is a prime number and returns True or False.

Usage:

    python3 prime.py
"""

from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
