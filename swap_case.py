def swap_case(s):
    res = " "
    for ch in s:
        asci = ord(ch)
        if asci >=65 and asci<=90:
            res = res +(chr(asci+32))
        else:
            res = res +(chr(asci-32))
    return res

if __name__ == '__main__':
    s1 = 'slient'
    s2 = 'listen'
    s1 = swap_case(s1)
    s2 = swap_case(s2)
    print(s1)
    print(s2)