side = int(input("Enter a number to indicate the size of the square: "))
ch = '*'
for i in range(side):
    for j in range(side):
        if i == 0 or i == side - 1 or j == 0 or j == side - 1:
            print(ch, end = '  ')
        else:
            print(' ', end = '  ')
    print()