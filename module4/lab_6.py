import math

def calc(x):
    y = math.log(1+2*math.exp(-x**2))*3/(x**2 + 4)
    return y

def calc_series(xn, xk, dx):
    x = xn
    X = []
    Y = [] 
    while x <= xk:
        y = calc(x)
        X.append(x)
        Y.append(y)
        print(f"x={x:.2f}, y={y:.4f}")
        x += dx
    return (X,Y)

# x, y = calc_series(0, 3, 0.2)
# print(x)
# print(y)
