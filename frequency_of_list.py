l = [12,23,34,23,12,23,34,12,56,12]
dict = {}
for key in l:
    if key in dict:
        dict[key] = dict[key]+1
    else:
        dict[key] = 1
print(dict)

for key in dict:
    print(key)#key
    print(dict[key])#values 
        