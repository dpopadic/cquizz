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
