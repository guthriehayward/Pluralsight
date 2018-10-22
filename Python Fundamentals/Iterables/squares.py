"""
Experimentation with square numbers using generators

Usage:
    python3 squares.py
"""
#Creates generators for the first 1 million perfect squares
million_squares = (x*x for x in range(1, 10000001))

#Format the output as a list
#Note: This will take 40mb of memory to run.
print(list(million_squares))

#Calculates the sum of these numbers.
sum(x*x for x in range(1, 10000001))
