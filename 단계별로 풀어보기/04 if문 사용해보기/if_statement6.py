inputNumber = int(input())

number = inputNumber
result = 0
count = 1

while True :
    if number < 10 :
        sum = number
        result = sum*10 + number
    else :
        sum = number//10 + number%10
        result = (number%10)*10 + sum%10

    if inputNumber == result :
        print(count)
        break
    else :
        count += 1 
        number = result
