i = 0
print("Начало цикла")
while i < 10:
    if i % 2 == 0:
        print(f"{i} - четное")
    else:
        print(f"{i} - нечетное")
    i += 1 # i = i + 1

print("Цикл закончил работу")

for i in range(0, 10, 2):
    print(i)


# Вычисление факториала
n = 6
res = 1
for i in range(1, n+1):
    res *= i

print(f"!{n} = {res}")
