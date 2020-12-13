while True:
    num = input('Enter:')
    if num == 'done':
        break
    else:
        x = int(num)
        if x > 7:
            y = x
            print(y,x)
        else:
            print(x)
