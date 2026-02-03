l = [90,80,70,92,42,91]

max1 = 90
max2 = 80

for i in range(2,len(l)):
    if l[i]>max1:
        max2 = max1
        max1 = l[i]
    elif l[i]>max2:
        max2 = l[i]
print(max2)