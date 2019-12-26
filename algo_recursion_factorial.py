# FACTORIAL (RECURSIVE FUNCTION) ---------------------------

def ffactorial(x):
    if(x == 0):
        res = 1
    else:
        res = x * ffactorial(x - 1)
    return(res)

ffactorial(2)
