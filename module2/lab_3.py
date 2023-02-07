import math
a = 3 # float(input("Введите a:"))
b = 3 # float(input("Введите b:"))
c = 2 # float(input("Введите c:"))
if a > 0 and b > 0 and c > 0:
    x = (abs(0.4*a - 2))**2 - 3*math.cos(b*c)
    y = math.log(abs(a*b*c/2)) - 1/(3*a)
    print(f"x = {x}, y = {y}")
else:
    print("Значения a b или с равны 0, повторите ввод")