import sys
input = sys.stdin.readline
n, m = map(int,input().split())

#중복 사용 방지
visited = [0] * (n + 1)

#현재 만들고 있는 순열 저장
permutation = []


def dfs(depth):
    
    #종료 조건
    if depth == m:
        print(*permutation)
        return
    
    #1~n까지 전부 후보로
    for i in range(1, n + 1):
        if not visited[i]:

            #선택
            visited[i] = 1
            permutation.append(i)

            #다음 단계
            dfs(depth + 1)

            #복구
            permutation.pop()
            visited[i] = 0

#처음엔 아무것도 선택 안했으니 0
dfs(0)