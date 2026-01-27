def check_happy(num): 
    res = 0 
    while (num!=0): 
        rem = num%10 
        res = (rem*rem)+res 
        num = num // 10 
    return res 
if __name__ == '__main__': 
    n = 7
    r = check_happy(n) 
    while r!=1 and r!=4: 
        r = check_happy(r)
    if r==1: 
        print("happy")
    if r == 4:
        print("not happy")