#주어진 리스트로 순열을 만든다
def perm(depth):
    if depth == m:
        print(*path)
        return
    
    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        path.append(arr[i])

        perm(depth + 1)

        visited[i] = False
        path.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()      #사전순 맞추기 위해 정렬

visited = [False] * n
path = []
perm(0)