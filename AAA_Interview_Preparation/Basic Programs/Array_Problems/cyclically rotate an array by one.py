# Program to cyclically rotate an array by one
# Last Updated : 11 Sep, 2023
# Given an array, the task is to cyclically rotate the array clockwise by one time.
#
# Examples:
#
# Input: arr[] = {1, 2, 3, 4, 5}
# Output: arr[] = {5, 1, 2, 3, 4}
#
# Input: arr[] = {2, 3, 4, 5, 1}
# Output: {1, 2, 3, 4, 5}

l = [2, 3, 4, 5, 1]
last_ele = l[-1]

for i in range(len(l)-1, -1, -1):
    l[i] = l[i-1]
l[0] = last_ele
print(l)

