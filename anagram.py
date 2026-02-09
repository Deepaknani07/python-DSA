def my_lower(l):
    res =" "
    for ch in l:
        asci = ord(ch)
        if asci >=65 and asci <=90:
            res += chr(asci+32)
        else:
            res +=ch
    return res



if __name__ == '__main__':
    s = 'liSTen'
    s1 = 'Slient'
    m = my_lower(s)
    m1 = my_lower(s1)
    print(m) 
    print(m1)   
    # if m == m1:
    #     print("anagram")
    # else:
    #     print("not anagram")