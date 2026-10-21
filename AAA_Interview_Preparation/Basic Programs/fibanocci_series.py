
s = 100

a = 0
b = 1
c = a+b
res = []
res.extend([a,b])

while c <= s:
    res.append(c)
    a = b
    b = c
    c = a+b

print(res)
