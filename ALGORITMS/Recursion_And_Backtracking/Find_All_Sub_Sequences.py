def sub_sequences(strings, jump, res):

    if jump > len(strings):
        return

    for i in range(len(strings)):
        temp = strings[i]
        if jump == 1:
            res.append(temp)

        for j in range(i+jump, len(strings)):
            temp += strings[j]
            res.append(temp)
    sub_sequences(strings, jump+1, res)


if __name__ == "__main__":
    strings = "sjvf"
    jump = 1
    res = []
    sub_sequences(strings, jump, res)
    #print(sorted(res))
    print(res)
