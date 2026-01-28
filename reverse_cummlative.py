def cum(l):
    sum = 0
    res = []
    for i in range(len(l)-1,-1,-1):
        sum = sum + l[i]
        res.append(sum)
    return res






if __name__ == '__main__':
    l = [3,5,7,6,4,9,2]
    c= cum(l)
    print(c)
    ans = []
    for i in range(len(c)-1,-1,-1):
        ans.append(c[i])
    print(ans)
        