inputNumber = int(input())

for i in range(inputNumber):
    for j in range(inputNumber):
        if  j < (inputNumber - i)-1:
            print(' ', end='')
        else :
            print('*', end='')
    print()
