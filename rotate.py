def rotate(l):
    temp = l[0]
    for i in range(1,len(l)):
        l[i-1] = l[i]
    l[len(l)-1] = temp
    print(l)

if __name__ == '__main__':
    l = [10,20,30,40,50]
    rotate(l)