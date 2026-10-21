num = 10234

res = 0

while num != 0:
    ele = num %10
    res += ele
    num = num//10
print(res)
