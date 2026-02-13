def expan(s):
    res = " "
    i =0
    while(i<len(s)):
        char = s[i]
        i += 1
        num = " "
        while i<len(s) and s[i].isdigit():
            num += s[i]
            i +=1
        res += char * int(num)
    print(res) 
        
if __name__ == '__main__':
    s = "a2b3c2"
    expan(s)