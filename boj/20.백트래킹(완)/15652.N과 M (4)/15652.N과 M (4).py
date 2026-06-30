import sys
input = sys.stdin.readline

n, m = map(int, input().split())

#중복조합이다.
cwr = []

def dfs(start):
    if len(cwr) == m:
        print(*cwr)
        return
    
    for i in range(start, n+1):
        cwr.append(i)
        dfs(i)      #자기 포함시켜도 된다.
        cwr.pop()

dfs(1)