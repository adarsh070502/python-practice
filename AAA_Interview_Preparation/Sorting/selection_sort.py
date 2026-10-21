l = [1,0, 88, 12, 15, 155, 3, 500]

n = len(l) - 1

for i in range(n):
    smallest = i
    for j in range(i+1, len(l)):
        if l[j] < l[smallest]:
            smallest = j

    temp = l[i]
    l[i] = l[smallest]
    l[smallest] = temp
print(l)


