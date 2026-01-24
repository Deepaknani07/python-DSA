def print_num(num):
    if num == 0:
        print(num)
        return
    print_num(num-1)
    print(num)
    
if __name__ == '__main__':
    n =5
    print_num(n)