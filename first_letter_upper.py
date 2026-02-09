def first_upper(s):
    res = ""
    for i in range(len(s)):
        if i ==0:
            ch = chr(ord(s[i])-32)
            res =res+ ch
        else:
            ch = s[i]
            res = res +ch
    print(res,end=" ")
    
if __name__ == '__main__':
    s = "dhee coding lab"
    arr = s.split()
    for x in arr:
        first_upper(x)
    