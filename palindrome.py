def palin(num):
    res = 0
    while (num !=0):
        rem = num %10
        res = (res *10)+rem
        num = num //10
    return res

if __name__ == '__main__':
    n = int(input("enter the number:"))
    r = palin(n)
    if n == r:
        print(f"{n} is a palindrome")
    else:
        print(f'{n} is not a palindrome')