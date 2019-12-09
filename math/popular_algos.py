import pandas as pd
import numpy as np

# The Time complexity or Big O notations for some popular algorithms are listed below..

# Binary Search: O(log n)
# Linear Search: O(n)
# Quick Sort: O(n * log n)
# Selection Sort: O(n * n)
# Travelling salesperson : O(n!)

# time and space complexity -----------------------------
# time complexity..
# First you need to investigate this question: “Which parts of my code become slower as the input size grows?”
# In analyzing the complexity of an algorithm, engineers use Big O notation. In our example above, the algorithm’s
# time complexity is O(n), where n is the number of items in the list.

# space complexity..
# Space Complexity measures memory and disk usage. A measure of the amount of working storage an algorithm needs. That
# means how much memory, in the worst case, is needed at any point in the algorithm

# example..
def example(word_list):
  all_words_with_a = [] # auxiliary space
  for word in word_list: # O(n) time complexity
    if word[0] == 'a':
      all_words_with_a.append(word)
  return all_words_with_a # O(n) space complexity


# BINARY SEARCH ------------------------------------------

def binary_search_iterative(array, item):
    #  create a variable for the left and right boundaries
    left_bound = 0 # left is the zero index of the array
    right_bound = (len(array) -1) # right is the full length of the array
    # as long as the left boundary is less than our equal to the right continue our search
    while left_bound <= right_bound:
        # cut the given current boundary and shorten the search with the current index always changing
        current_middle_index = ((left_bound + right_bound) // 2)
        middle_value = array[current_middle_index]
        # check if the middle index value is what we are searching for
        if middle_value == item:
            return current_middle_index
        # if the value is greater than move to left
        elif middle_value > item:
            right_bound = current_middle_index - 1
        # value is less than move to the right
        elif middle_value < item:
            left_bound = current_middle_index + 1
    # never found item - python and ruby we don't need a return
    return None


x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
s = 8
binary_search_iterative(x, item=s)


# SQUARE ROOT ALGO ---------------------------------------

def sq_root(number):
    x=number
    eps=1e-15
    if number == 0:
        x=0
    elif number < 0:
        print("There is no real solution for square roots of negative numbers.")

    while abs(x - number / x) > eps * x:
        x = (x + number / x) / 2
    return(x)

sq_root(2)

# in general function approximation..
def func(x):
    return x**2
def derivFunc(x):
    return 2*x
def newtonRaphson(x):
    h = func(x) / derivFunc(x)
    while abs(h) >= 0.0001:
        h = func(x) / derivFunc(x)
        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h
    return(x)
newtonRaphson(9)


# FACTORIAL (RECURSIVE FUNCTION) ---------------------------

def ffactorial(x):
    if(x == 0):
        res = 1
    else:
        res = x * ffactorial(x - 1)
    return(res)


ffactorial(2)

# UNIFORM TO NORMAL DISTRIBUTION TRANSFORMATION ------------

# 1. rank stocks from 1 to n
# 2. draw sample size of size n from standard normal
# 3. sort sample in descending order & assign stocks to the ranked stocks
# 4. repeat process 10.000 times & average results


def trans_unif_norm(x):
    """transform a rank from uniform to normal distribution."""
    xn = np.sort(x)[::-1]
    tmp = np.zeros([len(xn), 1000])
    for k in range(0, 1000):
        rn = np.random.normal(0, 1, len(xn))
        rn_s = np.sort(rn)[::-1]
        tmp[:, k] = rn_s

    y = tmp.mean(axis=1)
    z = y[x.argsort()]
    return(z)










