def rotate(l):
    last = l[len(l)-1]
    for i in range(len(l)-2,-1,-1):
        l[i+1] = l[i]
    l[0] = last
    print(l)

if __name__ == '__main__':
    l =[10,20,30,40,50]
    rotate(l)