l=[1,2,5,7,9,77,18]
min = l[1]
for i in range(len(l)):
    if l[i]<min:
        min = l[i]
print(min)