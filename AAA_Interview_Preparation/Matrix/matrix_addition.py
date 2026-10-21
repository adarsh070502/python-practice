
def matrix_addition(a, b):
    a_row_len = len(a)
    b_row_len = len(b)

    if a_row_len != b_row_len or a_row_len == 0:
        return []

    col_len = len(a[0])

    res = []
    for i in range(a_row_len):
        temp = []
        for j in range(col_len):
            a_temp = a[i][j]
            b_temp = b[i][j]
            temp.append(a_temp + b_temp)
        res.append(temp)
    return res


def main():
    a = [[1,2,3], [4,5,6], [7,8,9], [1,2,3]]
    b = [[7,8,9], [4,5,6], [7,8,9], [1,2,3]]

    res = matrix_addition(a,b)
    print(res)


if __name__ =="__main__":
    main()