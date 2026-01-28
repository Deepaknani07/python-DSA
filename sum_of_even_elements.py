def even(l,k):
    for i in range(len(l)):
        if  l[i]%2 == 0:
            k += l[i]
    return k 





if __name__ == '__main__':
    l =[3,5,7,6,4,9,2]
    k = 0
    e = even(l,k)
    print(e)