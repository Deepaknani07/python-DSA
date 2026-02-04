def sub_array(li):
    for i in range(len(li)):
        for j in range(i,len(li)):
            for k in range(i,j+1):
                print(li[k],end="")
            print()
            
if __name__ == '__main__':
    li = [1,2,3,4,5]
    sub_array(li)