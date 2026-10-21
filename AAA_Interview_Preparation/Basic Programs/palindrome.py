
def palindrome(s):
    i = 0
    j = len(s) - 1

    while i <= j:
        if s[i] != s[j]:
            return False
        else:
            i+=1
            j-=1
    return True


def main():
    s = "dagad"
    res = palindrome(s)

    if res:
        print("Palindrome")
    else:
        print("Not Palindrome")

main()
