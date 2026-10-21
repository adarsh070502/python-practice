# Find a peak element which is not smaller than its neighbours

# Input: array[]= {5, 10, 20, 15}
# Output: 20
# Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20.
#
# Input: array[] = {10, 20, 15, 2, 23, 90, 67}
# Output: 20 or 90
# Explanation: The element 20 has neighbors 10 and 15, both of them are less than 20, similarly 90 has neighbors 23 and 67.

l = [10, 20, 15, 2, 23, 90, 89]

if l[0] > l[1]:
    print(l[0])

elif l[-1] > l[-2]:
    print(l[-1])

else:
    for i in range(1, len(l)-1):
        if l[i] > l[i-1] and l[i] > l[i+1]:
            print(l[i])





