lis = [10, 11, 1, 12, 199, 87, 65, 43]
sear = 100
flag = True

for index in range(len(lis)):
    ele = lis[index]
    if ele == sear:
        print(index)
        flag = False
        break

if flag:
    print("Element not found")

