def l_search(l,key):
    for i in range(0,len(l)):
        if l[i] == key:
            return i
    return -1




if __name__ == '__main__':
    l = [1,2,3,4,5,6,7,8,9,10]
    key = 6
    index = l_search(l,key)
    print(index)