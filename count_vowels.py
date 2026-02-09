if __name__ == '__main__':
    s = "Dhee coding Lab"
    b = "aeiouAEIOU"
    count = 0
    for ch in s:
        if ch in b:
            count = count +1
    print(count)
            