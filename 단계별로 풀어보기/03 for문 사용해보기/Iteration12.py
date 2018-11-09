import sys

input = sys.stdin.readline

testSet = int(input())

for i in range(testSet):
    a , b = map(int, input().split())
    print(a+b)
