s = "adarsh"

method1 = s[-1::-1]
print(method1)

method2 = ""
string_length = len(s) - 1

for i in range(string_length, -1, -1):
    ele = s[i]
    method2+=ele
print(method2)