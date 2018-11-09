num = int(input())

lists = []

for x in range(num//3 + 1):
    for y in range(num//5 + 1):
        if (num == 3*x + 5*y) :
            lists.append([x,y])

if len(lists) == 0:
    print(-1)
    exit()

min = lists[0][0] + lists[0][1]
for i in range(len(lists)):
    sum = lists[i][0] + lists[i][1]
    if min > sum:
        min = sum

print(min)

