# A COLLECTION OF INTERESTING CODING PROBLEMS ---------------------------------------
import numpy as np

# --------------------------------------------
# Q1: Find all numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).
# difficulty level: 1
num_vec = np.arange(2000, 3201, 1)
x = num_vec[(num_vec %7 == 0) & (num_vec %5 != 0)]




