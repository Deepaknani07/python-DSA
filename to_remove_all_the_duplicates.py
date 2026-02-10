if __name__ == '__main__':
    s = 'malayalam'
    dict = {}
    for key in s:
        if key in dict:
            dict[key] = dict[key]+1
        else:
            dict[key] = 1
    print(dict)

for key in dict:
    # if (dict[key]==1):
        print(key)
            