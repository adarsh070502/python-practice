# Find Subarray with given Sum from Array of non-negative Numbers

# Input: arr[] = { 15, 2, 4, 8, 9, 5, 10, 23}, sum = 23
# Output: 2 5
# Explanation: Sum of elements between indices 2 and 5 is 2 + 4 + 8 + 9 = 23
#
# Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
# Output: 2 5
# Explanation: Sum of elements between indices 1 and 4 is 4 + 0 + 0 + 3 = 7
#
# Input: arr[] = {1, 4}, sum = 0
# Output: -1
# Explanation: There is no subarray with 0 sum

i = 0
j = 0
l = [15, 2, 4, 8, 9, 5, 10, 23]
desired_sum = 18
flag = False

temp_sum = l[0]
while j < len(l):

    if temp_sum == desired_sum:
        print(i+1)
        print(j+1)
        flag = True
        break

    elif temp_sum > desired_sum:
        temp_sum -= l[i]
        i+=1

    else:
        j+=1
        if j < len(l):
            temp_sum += l[j]

if not flag:
    print(-1)


