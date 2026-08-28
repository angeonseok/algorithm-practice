def sol(idx, alpha):
    global cnt

    #모든 알파벳이 담긴 시점부터는 그 뒤에 뭘 넣든 다 성립이 됨
    #idx 이후 남은 원소들로 부분집합 만드는 갯수만큼 더해주면 끝
    if len(alpha) == 26:
        cnt += 2 ** (n - idx)
        return

    if idx == n:
        return

    #idx번쨰 포함
    sol(idx + 1, alpha | arr[idx])

    #idx번째 미포함
    sol(idx + 1, alpha)


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [set(input().strip())for _ in range(n)]

    cnt = 0
    sol(0, set())
    print(f'#{tc} {cnt}')