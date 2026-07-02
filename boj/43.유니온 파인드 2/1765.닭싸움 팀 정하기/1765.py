#관계를 xor 연산으로 처리할라다 꼬임
#걍 그래프로 적을 저장하면 되지 않겠나 했다가 마지막에 꼬임

def find(x):
    while x != parent[x]:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x


def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra != rb:
        parent[rb] = ra


import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = list(range(n+1))
enemy = [[] for _ in range(n+1)]

for _ in range(m):
    rel, a, b = input().split()
    a = int(a)
    b = int(b)

    if rel == "F":
        union(a, b)
    
    else:
        enemy[a].append(b)
        enemy[b].append(a)

#모든 사람 보면서
for x in range(1, n+1):
    #나의 적을 찾고
    for e in enemy[x]:
        #나의 적의 적과
        for ee in enemy[e]:
            #합체
            union(x, ee)

#대표 기준으로 팀 개수 세기
team = set()
for i in range(1, n+1):
    team.add(find(i))

print(len(team))