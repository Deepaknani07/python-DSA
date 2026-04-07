if __name__ == '__main__':
    s = "aaabcddeee"
    l = []
    for ele in s:
        if l and l[-1] == ele:
            l.pop()
        else:
            l.append(ele)
    print(l)    