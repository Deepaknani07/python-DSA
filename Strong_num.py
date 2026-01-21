def factorial(num):
    res = 1
    for i in range(1,num+1):
        res = res* i
    return res

def strong(num):
    ans = 0
    while (num !=0):
        rem = num % 10
        ans = factorial(rem)+ans
        num = num //10
    return ans

if __name__ == '__main__':
    n = int(input("enter the number:"))
    s = strong(n)
    if n == s:
        print(f"{n} is strong number")
    else:
        print(f"{n} is not a strong number")