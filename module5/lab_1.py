import math 
def calc_active(E0, k, t):
    E = E0 * math.exp(-k*t)
    return E

t = 4

act1 = calc_active(2, 3, t)
act2 = calc_active(1, 3, t)
act3 = calc_active(3, 2, t)

res = (act1 + act2 + act3)/3
print(f"Средняя активность равна {res}")


# Улучшенный вариант решения
activities = [[2, 5], [1,4], [3,6], [2, 4], [3, 3]]
sum = 0
for act in activities:
    sum += calc_active(act[0], act[1], t)
res = sum/len(activities)
print(f"Средняя активность равна {res}")

activities = [
    {
        "E0": 2,
        "k": 5
    },
    {
        "E0": 3,
        "k": 4
    },
    {
        "E0": 1,
        "k": 5
    },
    {
        "E0": 5,
        "k": 9
    },
]

sum = 0
for act in activities:
    sum += calc_active(act["E0"], act["k"], t)
res = sum/len(activities)
print(f"Средняя активность равна {res}")