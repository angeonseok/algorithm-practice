import sys
input = sys.stdin.readline

n = int(input())

name_list = []
for _ in range(n):
    name = input().split()
    name_list.append(name)

#리스트 첫 항만 오름차순. 리스트 내용물 str이라 int형 정렬 기준으로 변경
name_list.sort(key=lambda x : int(x[0]))

for i, j in name_list:
    print(i, j)