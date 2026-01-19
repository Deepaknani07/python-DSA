def countfact(num):
    count = 0
    while (num!=0):
        num = num //10
        count = count +1
    return count

def arm(num):
    res = 0
    count = countfact(num)
    while (num!=0):
        rem = num % 10
        res = res + rem ** count
        num = num // 10
    return res

if __name__ == '__main__':
    # n = int(input("enter the number:"))
    for i in range(1,10000):
        n = i
        a =arm(n)
        print(a)
        if (n==a):
            print(f"{n} is a armstrong number")
            
        