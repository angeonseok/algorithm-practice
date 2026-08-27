def sol(depth, l, r):
    global cnt

    #모든 친구들을 다 쓰면 ㅇㅋ
    if depth == n:
        cnt += 1
        return

    #모든 애들을 쓸거다.
    for i in range(n):
        #이미 뽑힌 놈은 컽
        if used[i]:
            continue
        
        used[i] = True

        #기본적으로는 왼쪽에 더한다.
        sol(depth + 1, l + arr[i], r)

        #만약 오른쪽에 더할 수 있다면 거기도 해본다.
        if r + arr[i] <= l:
            sol(depth + 1, l, r + arr[i])
            
        used[i] = False 


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    used = [False] * n
    cnt = 0
    sol(0, 0, 0)

    print(f'#{tc} {cnt}')