def neon(num):
    sq = num * num
    res = 0
    while(sq!=0):
        rem = sq % 10
        res = res + rem
        sq = sq // 10
    return res == num

if __name__ == '__main__':
    n = int(input("enter the number :"))
    if neon(n):
        print(f"{n} is neon number")
    else:
        print(f"{n} is not a neon number")