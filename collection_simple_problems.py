# A COLLECTION OF INTERESTING CODING PROBLEMS ---------------------------------------
# difficulty levels range from 1 (simple) - 3 (hard)
import numpy as np

# --------------------------------------------
# Q1: Find all numbers which are divisible by 7 but are not a multiple of 5, between 3000 and 4300 (both included).
# difficulty level: 1
num_vec = np.arange(3000, 4301, 1)
x = num_vec[(num_vec %7 == 0) & (num_vec %5 != 0)]


# --------------------------------------------
# Q2: Write an algo that goes through a list in rolling k windows and stores the results in another list, with the
# elements sorted in increasing order.
# difficulty level: 1
ax = [5, 3, 6, 8, 9, 12, 5, 1, 7]
a = []
k = 3
for j in range(0, len(ax)-k+1):
    a.append(np.sort(ax[j:(j+k)]))


# --------------------------------------------
# Q3: Write a program that computes the factorial given a number.
# difficulty level: 1

def comp_factorial(x):
    if x == 0:
        y = 1
    else:
        y = x * comp_factorial(x-1)
    return(y)

comp_factorial(4)


# --------------------------------------------
# Q4: Given an integer n, write a program that returns a dictionary that contains i, i*i where i ranges from 1 to n.
# difficulty level: 1
n = 8
d = {i: i**2 for i in range(1, n+1)}


# --------------------------------------------
# Q5: Define a class which has at least two methods:
# getString: to get a string from console input and printString: to print the string in upper case
# Also include a simple test function to test the class methods.
# difficulty level: 1

class StrInOut(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())

so = StrInOut()
so.getString() # type: this is my string
so.printString()
















