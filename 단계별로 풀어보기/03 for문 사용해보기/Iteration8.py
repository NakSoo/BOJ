week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
monthes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month, day = map(int, input().split())

days = 0

for i in range(month-1):
    days += monthes[i]

days += day

print(week[days%7])
