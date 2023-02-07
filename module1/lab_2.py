boolean_variable = True
print(boolean_variable)

boolean_variable = False
print(boolean_variable)

a = 5
b = 4
print(a/b)

str_var = "Hello\nworld"
print(str_var)

width = 5
height = 6
square = width * height
print("Площадь прямоугольника шириной", width, "см. и высотой", height, "см. равна", square, "см^2" )

answer = "Площадь прямоугольника шириной " + str(width) + " см. и высотой " + str(height) + " см. равна " + str(square) + " см^2"
print(answer)

answer = f"Площадь прямоугольника шириной {width} см. и высотой {height} см. равна {square} см^2"
print(answer)

a = 5
print(a, type(a))
a = 5.5
print(a, type(a))
a = "hello"
print(a, type(a))