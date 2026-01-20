def perfect(num):
    res =0
    for i in range(1,num):
        if num % i == 0:
            res = res + i
    return res

if __name__ == '__main__':
    n = int(input("enter the number:"))
    p = perfect(n)
    if n== p:
        print(f"{n} is perfect num")
    else:
        print(f"{n} is not perfect number")