
def matrix_multiplication(a, b):
    a_row_len = len(a)
    b_row_len = len(b)

    a_col_len = len(a[0])
    b_col_len = len(b[0])

    # To multiply one matrix with another, we need to check first,
    # if the number of columns of the first matrix is equal to the number of rows of the second matrix.
    if a_col_len != b_row_len:
        return []

    res = []
    for i in range(a_row_len):
        temp_lis = []
        for j in range(b_col_len):
            temp = 0
            for k in range(b_row_len):
                temp += a[i][k] * b[k][j]
            temp_lis.append(temp)
        res.append(temp_lis)
    return res


def main():
    a = [[1,2,3], [4,5,6], [7,8,9]]
    b = [[7,8,9], [4,5,6], [7,8,9]]

    res = matrix_multiplication(a, b)
    print(res)


if __name__ =="__main__":
    main()