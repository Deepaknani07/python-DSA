def my_lower(str):
    res =""
    for i in str:
        asci = ord(i)
        if asci >=65 and asci <=90:
            res = res + chr(asci+32)
        elif asci >=97 and asci <= 122:
            res = res + chr(asci-32)
    return res





if __name__ == '__main__':
    s = 'Slient'
    s1 = 'ListEN'
    m = my_lower(s)
    m1 = my_lower(s1)
    print(m)
    print(m1)
