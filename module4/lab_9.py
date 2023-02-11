import math
def calc(x):
    p = 1
    for x_i in x:
        p *= (2+ math.cos(x_i**2))
    print(f"P={p}")

def second(z):
    s = 0
    for z_i in z:
        s += math.exp(-2*z_i)*math.log(abs(z_i))
    print(f"S={s}")

calc([1,2,3,4,5])
second([ 0.1, 0.2,0.3, 0.4,  0.5])