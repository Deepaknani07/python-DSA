def countfact(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count +=1
    return count
# for loop
# if __name__ == '__main__':
#     count = 0 
#     for n in range(1,10000):
#         p = countfact(n)
#         if p ==2:
#             print(n)
#             count += 1
#         if count == 50:
#             break

#while loop

if __name__ == '__main__':
    count = 0
    i = 1
    while True:
        n =i
        p = countfact(n)
        if p ==2:
            print(n)
            count +=1
        i = i+1
        if count == 50:
            break