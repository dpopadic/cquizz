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




