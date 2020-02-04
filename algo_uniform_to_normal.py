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

# example..
import numpy as np
x = np.sort(np.random.random_integers(1, 1000, 100))
x = np.random.random_integers(1, 1000, 100)
y = trans_unif_norm(x)
