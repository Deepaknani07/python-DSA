def harshad_num(num):
    res = 0 
    
    while (num !=0):
        
        rem = num % 10
        res = res + rem
        num = num// 10
    return res

if __name__ == '__main__':
    n = int(input("enter the number:"))
    h = harshad_num(n)
    if (n % h == 0):
        print(f"{n} is a harshad number")
    else:
        print(f"{n} is not harshad number")