def reverse(num):
    res = 0
    while (num !=0):
        rem = num % 10
        res = (res*10)+rem
        num = num//10
    return res

if __name__ == '__main__':
    n = int(input("Enter the number:"))
    r = reverse(n)
    print(r)