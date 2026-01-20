def perfect(num):
    res =0 
    for i in range(1,num):
        if num % i ==0:
            res = res + i
    return res

if __name__ == '__main__':
    for i in range(1,10000):
        n = i
        p = perfect(n)
        if n == p:
            print(n)