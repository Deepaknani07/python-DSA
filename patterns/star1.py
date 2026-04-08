if __name__ == '__main__':
    rows = 5
    for i in range(1,rows + 1):
        for j in range(rows + 1-i,rows+1):
            print(j,end="")
        print()