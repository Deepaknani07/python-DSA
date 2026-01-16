def pal(num):
    res = 0
    while num !=0:
        rem = num %10
        res = (res * 10) + rem
        num = num //10
    return res 

if __name__ == '__main__':
    for i in range(1,10000):
        n = i
        r = pal(n)
        if n == r:
            print(n)