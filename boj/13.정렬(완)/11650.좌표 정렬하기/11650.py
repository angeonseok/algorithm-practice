import sys
input = sys.stdin.readline

n = int(input())

num_list = []
for _ in range(n):
    [a, b] = map(int,input().split())
    num_list.append([a, b])

#sort는 기본적으로 오름차순
num_list.sort()

for i in num_list:
    print(i[0], i[1])