# Find the largest sequence of 1's in 0 and 1 array

l = [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

index = 0
list_len = len(l)
largest_sequence = 0

while index < list_len:

    if l[index] == 1:
        temp_largest_sequence = 1
        j = index+1

        while j < list_len:
            if l[j] == 1:
                temp_largest_sequence += 1

            if l[j] == 0:
                index = j
                break
            j+=1
        if temp_largest_sequence > largest_sequence:
            largest_sequence = temp_largest_sequence
    index += 1

print(largest_sequence)


