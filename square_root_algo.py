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

