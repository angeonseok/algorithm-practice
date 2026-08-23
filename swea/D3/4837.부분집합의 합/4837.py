def sol(idx, path):
    global cnt

    #원소 n개면 멈춰서 검사
    if len(path) == n:
        if sum(path) == k:
            cnt += 1
        return

    #원소는 1~12라 걍 여기서 처리
    for i in range(idx, 13):
        path.append(i)
        sol(i + 1, path)
        path.pop()    

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())

    cnt = 0

    #첫 원소가 1인걸 기억해야한다
    sol(1, [])

    print(f'#{tc} {cnt}')