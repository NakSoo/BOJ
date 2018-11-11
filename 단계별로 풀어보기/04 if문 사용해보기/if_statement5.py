testCase = int(input())
for i in range(testCase):
    lists = []
    lists.extend(map(int, input().split()))
    sum = 0
    for j in range(len(lists)-1):
        sum += lists[j+1]
    average = sum / lists[0]

    count = 0
    for k in range(len(lists)-1):
        if(lists[k+1] > average):
            count += 1

    print('%.3f%%'% ((count/lists[0])*100))