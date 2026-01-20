def get_cont(num):
    count = 0
    while num != 0:
        num = num//10
        count = count +1
    return count

def deserium(num):
    sum = 0
    while num !=0:
        rem = num % 10
        sum = sum + rem ** (get_cont(num))
        num = num //10
    return sum

if __name__ == '__main__':
    n = int(input("enter the number:"))
    d =deserium(n)
    if n==d:
        print(f"{n} is a deserium number")
    else:
        print(f"{n} is not a desrium numbers")