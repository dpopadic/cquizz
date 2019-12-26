# ROLLING SORTING ALGO --------------------------------------------
import numpy as np
ax = [5, 3, 6, 8, 9, 12, 5, 1, 7]
a = []
k = 3
for j in range(0, len(ax)-k+1):
    a.append(np.sort(ax[j:(j+k)]))
