def neon(num):
    res = 0
    while(num!=0):
        rem = num% 10
        res = res + rem
        num = num // 10
    return res 

if __name__ == '__main__':
    n = int(input("enter the number :"))
    d=neon(n*n)
    if n==d:
        print(f"{n} is neon number")
    else:
        print(f"{n} is not a neon number")