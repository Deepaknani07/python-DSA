def countfact(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count +=1
    return count

def palin(num):
    res = 0
    while(num !=0):
        rem = num % 10
        res = (res* 10 )+ rem
        num = num //10
    return res

if __name__ == '__main__':
    n = int(input("enter the number:"))
    fact1 = countfact(n)
    rev = palin(n)
    fact2 = countfact(rev)
    if (fact1 ==2 and fact2 ==2 and rev !=0):
        print(f"{n} is ia erimp")
    else:
        print(f"{n} is not a erimp")