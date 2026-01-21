def smallest(num):
    res = 0 
    while(num!=0):
        rem = num % 10
        res = rem + res
        num = num // 10
    return res

if __name__ == '__main__':
    n =10
    n1 =n+1
    while (smallest(n)*2 != smallest(n1)):
        n1 = n1 +1                
    print(n1)
        