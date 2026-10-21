
def binary_search(lis, sear):

    i = 0
    j = len(lis)

    while i <= j:
        mid = (i+j)//2
        ele = lis[mid]

        if ele == sear:
            return mid
        elif ele > sear:
            j = mid-1
        else:
            i = mid+1
    return -1


def main():
    lis = [1, 13, 25, 36, 47, 88]
    sear = 88
    res = binary_search(lis, sear)

    if res != -1:
        print(res)
    else:
        print("Element not found")

main()