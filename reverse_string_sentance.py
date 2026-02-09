def reverse(s):
    res = " "
    for ch in s:
        res = ch + res
    return res

if __name__ == '__main__':
    s =  "dhee coding lab"
    res = " "
    arr = s.split()
    for st in arr:
        res = res + reverse(st)+''
    print(res)
