print(5 == 4)
print(5 >= 4)

a = 4
b = 3 
c = 0
print(a > 0 or b >0 or c > 0)
print(a > 0 and b >0 and c > 0)

age = 21
if age < 7:
    print("дошкольник")
elif age >=7 and age <18:
    print("Школьник")
elif age >= 18 and age < 22:
    print("Студент")
elif age >= 22:
    print("Работник")   
else:
    print("Не правильно введен возраст")
print("Finish")