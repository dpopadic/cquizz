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
