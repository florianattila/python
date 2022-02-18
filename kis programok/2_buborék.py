t = [5, 3, 42, 12, 6, -4]
n = len(t)
for i in range(n-1, 0, -1):
    for j in range(0,i):
        if t[j] > t[j+1]:
            tmp = t[j+1]
            t[j+1] = t[j]
            t[j] = tmp
print(t)