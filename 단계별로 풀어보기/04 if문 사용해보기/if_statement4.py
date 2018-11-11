number = int(input())
lists = []
lists.extend(map(int, input().split()))

maxNum = max(lists)
for i in range(len(lists)):
    lists[i] = (lists[i]/maxNum)*100

print('%.2f' % (sum(lists)/len(lists)))