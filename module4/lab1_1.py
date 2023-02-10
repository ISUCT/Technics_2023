e = 0.001
i = 0
res = 0
while True:
    x = ((-1)**i)/(2*i+1)
    res = res + x
    i += 1
    if abs(x) < e:
        print(res*4, x)
        break
    
    
print("calculation finished")