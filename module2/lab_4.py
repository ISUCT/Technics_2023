import math
x = 5
a = 1 
b = 4
print("before if")
if a > 0:
    print("a > 0")
    y = 0
    if x**(1/2) > abs(a*b):
        print("first formula")
        znam = (a**5 * math.cos(b)**2)
        y = 3*math.cos(1/znam)**2
    else:
        print("second formula")
        y = (abs(2*math.cos(x)**3 - 5*math.sin(x)**2 + a*b))**(1/2)
    
    f = 2* x**2 * math.log(y)
    print(f"f = {f}")
else:
    print("a < 0")