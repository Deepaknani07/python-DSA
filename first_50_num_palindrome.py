def palin(num):
    res = 0
    while (num!=0):
        rem = num % 10
        res = (res *10) + rem
        num  = num // 10
    return res
        # for loop
# if __name__ == '__main__':
#     count = 0
#     for i in range(1,10000):
#         n = i
#         r = palin(n)
#         if n == r:
#             print(n)
#             count += 1
#         if count == 50:
#             break

# while loop

if __name__ == '__main__':
    count = 0
    i =1
    while True:
        n = i
        r = palin(n)
        if n == r:
            print(n)
            count +=1
        i= i+1
        if count == 50:
            break
        