if __name__ == '__main__':
    a = "hello"
    res = ""
    for i in a:
        res = i + res
    print(res)
    if a == res:
        print("palindrome")
    else:
        print("not palindrome")