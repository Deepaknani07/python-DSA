def b_serach(l,key):
    low = 0
    high = len(l)-1
    while low <= high:
        mid = (low+high) //2    
        if l[mid] == key:
            return mid
        elif key > l[mid]:
            low = mid+1
        else:
            high = mid -1
    return -1
    
    
    
    
    
if __name__ == '__main__':
    l = [10,20,30,40,45,50,60,70]
    key = 30
    b = b_serach(l,key)
    print(b)
    