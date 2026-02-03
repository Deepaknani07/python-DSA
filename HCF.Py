a =12
b = 24
min_val = 0
if a<b:
    min_val = a
else:
    min_val = b
hcf =1
for i in range(1,min_val+1):
    if(a%i == 0 and b%i == 0):
        hcf = i
print(hcf)