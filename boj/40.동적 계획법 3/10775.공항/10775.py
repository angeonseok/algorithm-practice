import sys
input = sys.stdin.readline

# 유니온 파인드로 도킹 가능한 가장 큰 게이트 관리
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

g = int(input())
p = int(input())

# parent[x] = x 이하에서 현재 도킹 가능한 가장 큰 게이트
parent = [i for i in range(g + 1)]

cnt = 0
for i in range(p):
    a = int(input())

    # a번 이하에서 도킹 가능한 게이트 찾기
    ga = find(a)

    # 0이면 더 이상 도킹 불가능
    if ga == 0:
        break
    
    # ga는 이제 사용했으니까
    # 다음부터는 그 아래 구간의 대표 게이트를 보게 함
    parent[ga] = find(ga - 1)
    cnt += 1

print(cnt)