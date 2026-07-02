import sys
input = sys.stdin.readline

n, m = map(int,input().split())

#이번엔 중복순열이다. visited 만들어서 중복 체크할 이유가 없다
pwr = []

def dfs(depth):
    if depth == m:
        print(*pwr)
        return
    
    for i in range(1, n+1):
        pwr.append(i)

        dfs(depth + 1)

        pwr.pop()

dfs(0)