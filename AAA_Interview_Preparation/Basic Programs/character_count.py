
s = "adarshadarsh"
res = dict()

for ele in s:
    if ele not in res.keys():
        res[ele] = 1
    else:
        res[ele] = res[ele] + 1
print(res.items())

