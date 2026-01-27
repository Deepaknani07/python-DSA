def rev_rec(num,res):
    if num%10 == 0:
        return res
    
    rev = rev_rec(num//10,res*10+num%10)
    return rev

if __name__ == '__main__':
    n = 1234
    r = rev_rec(n,res = 0)
    print(r)
    