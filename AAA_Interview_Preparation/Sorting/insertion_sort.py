l = [1, 0, 88, 12, 15, 155, 3, 500]

for i in range(1, len(l)):
    curr = l[i]
    j = i-1

    while j >= 0 and curr < l[j]:
        l[j+1] = l[j]
        j -= 1
    l[j+1] = curr
print(l)

