import sys
input = sys.stdin.readline

def perm(depth):
    if len(path) == m:
        print(*path)
        return
    
    temp = 0    #같은 depth에서 중복 수열 막기용
    for i in range(n):

        #이미 쓴 놈 + 같은 depth에서 같은 값 쓰면 스킵
        if visited[i] or arr[i] == temp:
            continue
        
        visited[i] = True 
        path.append(arr[i])
        temp = arr[i]

        perm(depth+1)
        
        visited[i] = False
        path.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

visited = [False] * n
path = []
perm(0)