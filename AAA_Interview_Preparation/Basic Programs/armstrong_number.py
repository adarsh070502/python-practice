num = 153
num1 = num

res = 0
while num1 > 0:
    temp = num1 % 10
    res += (temp**3)
    num1 = num1//10

if res == num:
    print("Armstrong number")
else:
    print("Not")

