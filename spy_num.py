def spy(num):
    res = 0
    res1 = 1
    while(num!=0):
        rem = num % 10
        res = res + rem
        res1= res1 * rem
        num = num // 10
    return res == res1
        
if __name__ == '__main__':
    n = int(input("enter the number:"))
    
    if spy(n) :
        print("spy")
    else:
        print("not spy")
