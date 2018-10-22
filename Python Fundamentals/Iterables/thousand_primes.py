"""
    Generates a list of the first 1000 prime numbers,
    and then calculates their sum.

    Note: requires prime.py.

    Usage:
        python3 thousand_primes.py
"""

from itertools import islice, count
from prime import is_prime

#Creates first thousand primes
thousand_primes = (islice((x for x in count() if is_prime(x)), 1000)

#Puts them into a list
print(list(thousand_primes))

#Calculates the sum
sum(islice((x for x in count() if is_prime(x)), 1000))
