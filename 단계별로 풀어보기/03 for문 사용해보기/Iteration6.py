inputNumber = int(input())

for i in range(inputNumber):
    for j in range(inputNumber):
        if  j < inputNumber - i:
            print('*', end='')
    print()
