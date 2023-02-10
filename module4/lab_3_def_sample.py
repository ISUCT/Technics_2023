import math

def calc(xn, xk, dx):
    x = xn
    X = []
    Y = [] 
    while x <= xk:
        y = math.log(1+2*math.exp(-x**2))*3/(x**2 + 4)
        X.append(x)
        Y.append(y)
        print(f"x={x:.2f}, y={y:.4f}")
        x += dx
    return(X,Y)

xn = 0
xk = 3
dx = 0.2
x, y = calc(xn, xk, dx)
print(x)
print(y)