def spy(num):
    ans = 0
    ans1 = 1
    while(num!=0):
        rem = num % 10
        ans = ans +rem
        ans1 = ans1 * rem
        num = num // 10
    if ans == ans1:
        return True
    return False

if __name__ == '__main__':
    n = int(int(input("enter the number:")))
    if spy(n) == True:
        print("the number is spy")
    else:
        print("the number is not spy")