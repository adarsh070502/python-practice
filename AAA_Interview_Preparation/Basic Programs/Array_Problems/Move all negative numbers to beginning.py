#Move all negative numbers to beginning


# An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.
#
# Examples :
#
# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5

l = [-12, 11, -13, -5, 6, -7, 5, -3, -6]

index = 0

for i in range(len(l)):
    ele = l[i]
    if ele < 0:
        temp = l[index]
        l[index] = l[i]
        l[i] = temp
        index+=1
print(l)

