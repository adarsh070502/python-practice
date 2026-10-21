l = [1,0, 88, 12, 15, 155, 3, 500]

n = len(l) - 1

for i in range(n):
    for j in range(0, n-i):
        if l[j] > l[j+1]:
            temp = l[j]
            l[j] = l[j+1]
            l[j+1] = temp
print(l)