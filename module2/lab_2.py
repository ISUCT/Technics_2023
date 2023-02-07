x = float(input("x="))
y = float(input("y="))
R = float(input("R="))

length = (x**2 + y**2)**(1/2.0)
if length < R:
    print(f"Точка с координатами M({x},{y}) лежит в круге радиуса R = {R}")
else:
    print(f"Точка с координатами M({x},{y}) не лежит в круге радиуса R = {R}")