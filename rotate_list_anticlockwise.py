l = [10,20,30,40,50]
k =2
res = [0] * len(l)
for i in range(len(l)):
    res[(i-k)%len(l)] = l[i]
print(res)