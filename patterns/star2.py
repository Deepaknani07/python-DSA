rows =5
for i in range(1, rows+1):
    for j in range(rows, i-1,-1):
        print(j,end="")
    print()