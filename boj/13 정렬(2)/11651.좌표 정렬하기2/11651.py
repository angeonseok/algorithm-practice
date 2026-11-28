import sys
input = sys.stdin.readline

n = int(input().rstrip())

num_list = []
for _ in range(n):
    [a, b] = map(int,input().split())
    num_list.append([a, b])

#key=lambda를 이용해 정렬조건 변경 가능. 1항 오름차순 > 0항 오름차순
num_list.sort(key= lambda x : (x[1],x[0]))

for i in num_list:
    print(i[0], i[1])