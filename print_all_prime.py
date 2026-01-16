def countfact(num):
    count = 0
    for i in range(1,num+1):
        if num % i == 0:
            count +=1
    return count
            
if __name__ == '__main__':
    for n in range(1,10000):
        p =  countfact(n)
        if p ==2:
            print(n)