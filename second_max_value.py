l = [90,80,70,92,42,91]

if l[0]>l[1]:
    max1 = l[0]
    max2 = l[1]
else:
    max1 = l[1]
    max2 = l[0]

for i in range(2,len(l)):
    if l[i]>max1:
        max2 = max1
        max1 = l[i]
    elif l[i]>max2:
        max2 = l[i]
print(max2)