import sys
input = sys.stdin.readline

n, m = map(int,input().split())

#이번엔 조합이다
combination = []

def dfs(start):
    if len(combination) == m:
        print(*combination)
        return
    
    for i in range(start, n+1):
            combination.append(i)

            dfs(i+1)

            combination.pop()

#처음엔 1부터 골라야지
dfs(1)