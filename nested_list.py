if __name__ == '__main__':
    l = [1,2,[3,4],5,6,[7,8],9]
    t = []
    count = 0
    for ele in l:
        var = ele
        if type(var) == list:
            for i in var:
                t.append(i)
                count +=1
        else:
            t.append(var)
            count +=1
    print(t)