import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    rootA = find(a)
    rootB = find(b)

    if rootA != rootB:
        parent[rootB] = rootA
    
n = int(input())
m = int(input())

parent = [i for i in range(n+1)]
arr = [list(map(int,input().split())) for _ in range(n)]

#연결 됨(1) 상태면 인덱스 확인해서 같은 집합으로 묶기
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            union(i+1, j+1)

#루트노드간 비교를 통해 주어진 도시간 연결 확인
t_list = list(map(int,input().split()))
for i in range(len(t_list)):
    t_list[i] = find(t_list[i])

#루트노드가 전부 같으면 이동가능
flag = True
for j in range(m-1):
    if t_list[j] != t_list[j+1]:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')