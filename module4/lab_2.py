#    0    1    2   3
a = [100, 20, 30, 45, 50, 67, 84, 59]
#                     -4  -3  -2  -1
print(a)
print(a[0])
print(a[3])
print(f"len = {len(a)}")
print(a[len(a)-1])
print(a[-1])

b,c,d = [1,2,3]
print(c)

print(a[0:3])
print(a[2:5])
print(a[3:])
print(a[:5])

a.append(5555)
a[0] = -100
print(a)
a.extend([1,2])
print(a)

idx = a.index(5555)
print(idx)
try:
    idx = a.index(-5555)
except:
    print("failed")
print(idx)

res = sorted(a)
print(a)
print(res)

for item in a:
    print(item)