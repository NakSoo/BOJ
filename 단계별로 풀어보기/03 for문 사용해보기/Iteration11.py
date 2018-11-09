inputString = input()

length = len(inputString)

for i in range(0, length, 10):
    print(inputString[i:i+10])