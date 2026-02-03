a = 12
b = 24
max_val = 0
if  a>b:
    max_val = a
else:
    max_val = b
lcm =1
for i in range(max_val,(a*b)+1):
    if i%a == 0 and i%b == 0:
        lcm = i
        break
print(lcm)