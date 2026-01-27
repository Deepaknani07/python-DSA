def countfact(num):
    count = 0 
    while (num!=0):
        num = num//10
        count += 1
    return count


def desire(num):
    count = countfact(num)
    res = 0
    while (num!=0):
        rem = num % 10
        res = res + rem ** count
        count -=1
        num = num // 10
    return res

if __name__  == '__main__':
    n = int(input("enter the number:"))
    a =desire(n)
    if n == a:
        print(f"{n} is a desire")
    else:
        print(f"{n} is not a desire")
