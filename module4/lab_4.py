import math
x= 0.5

def calc():
    y = math.log(1+2*math.exp(-x**2))*2/(x**2 + 4)
    print(x, y)

calc()


x = 0.9
calc()

x = 1.2
calc()