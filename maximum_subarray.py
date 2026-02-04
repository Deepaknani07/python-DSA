def sub_array(li):
    max = li[0]
    for i in range(len(li)):
        for j in range(i,len(li)):
            sum = 0
            for k in range(i,j+1):
                sum += li[k]
            if (sum > max):
                max = sum
    print(max)

if __name__ == '__main__':
    li = [-1,-2,-3,-4,-5]
    sub_array(li)