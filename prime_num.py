def countfact(num):
    count = 0 
    for i in range(1,num+1):
        if num % i == 0:
            count +=1
    return count

if __name__ == '__main__':
    n = int(input("enter the number:"))
    c = countfact(n)
    if c == 2:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")