def sub_array(li,k1):
    max = 0
    sum = 0
    for i in range(0,k1):
        sum +=li[i]
    max = sum
    sum =0
    for i in range(len(li)):
        for j in range(i,len(li)):
            sum = 0
            leng = 0
            for k in range(i,j+1):
                sum += li[k]
                leng += 1
            if (sum > max and leng == k1):
                max = sum
    print(max)

if __name__ == '__main__':
    li = [-1,1,-3,-4,-5]
    k1 =2
    sub_array(li,k1)