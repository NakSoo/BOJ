n , x = map(int, input().split())

numbers = []

numbers.extend(map(int, input().split()))

for i  in range(len(numbers)):
    if numbers[i] < x :
        print(numbers[i], end=' ')
