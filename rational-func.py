def rational_make(n, d):
    return (n, d)

def numer(x):
    return x[0]

def denom(x):
    return x[1]

def rational_add(x, y):
    return rational_make(numer(x) * denom(y) + numer(y) * denom(x),
                         denom(x) * denom(y))

def rational_repr(x):
    return "{}/{}".format(numer(x), denom(x))

if __name__ == '__main__':

    half  = rational_make(1, 2)
    third = rational_make(1, 3)

    total = rational_add(half, third)

    print "{} + {} = {}".format(*map(rational_repr, (half, third, total)))
