cipher = int(input())
inputNumber = int(input())

sum = 0
temp = inputNumber

for i in range(cipher):
    sum += temp%10
    temp = temp//10
print(sum)