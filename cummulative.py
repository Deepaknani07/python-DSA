def cumm(l):
    sum = 0
    res =[]
    for i in range(len(l)):
        sum = sum + l[i]
        res.append(sum)
    return res




if __name__ == '__main__':
    l  = [3,5,7,6,4,9,2]
    c = cumm(l)
    print(c)