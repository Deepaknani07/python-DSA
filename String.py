if __name__ == '__main__':
    a = 'hello'
    print(a[1:4])
    print(a[::2])
    print(a[::-1])
    print(a[::-2])
    print(a[0:4:1])
    print(a[0:4:-1])
    
    for ch in a:
        print(ch)

    for i in range(len(a)):
        print(a[i])
        
    a1 = 'world'
    print(a+a1)
    print(a*4)
    print('l' in a1)
    print('a' in a1)
    