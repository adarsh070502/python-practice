
num = 10002156
res = 0

while num != 0:
    temp = num % 10
    res = res*10 + temp
    num = num // 10
print(res)