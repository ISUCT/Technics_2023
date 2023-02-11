# 7
x = [
    [1, -2,  3,4, -9, 8],
    [2,  2, -5,4,  9, -8],
    [1,  2,  3,4, -5, 6],
    [-1,-2,  0,4, -3, 8],
    ]

def calculate(x):
    negative_count = []
    for i in range(len(x[0])):
        negative_count.append(0)

    for line in x:
        i = 0
        for item in line:        
            if item <0:
                negative_count[i] += 1
            i += 1
    return negative_count

result = calculate(x)
print(result)

a = [
    [-1, -2,  3, -4],
    [-2,  2, -5, -4],
    [ 1,  2,  3, -4],
    ]

print(calculate(a))