def sol(depth, cursum):
    global ans

    #가지치기
    if cursum >= ans:
        return

    #위에서 함 걸렀으니 이놈으로 갱신 가능함
    if cursum >= s:
        ans = cursum
        return

    #끝까지 다 돌면 종료조건
    if depth == n:
        return

    #depth번째 원소 포함하는 경우
    sol(depth + 1, cursum + arr[depth])

    #미포함하는 경우
    sol(depth + 1, cursum)


T = int(input())
for tc in range(1, T+1):
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = float('inf')
    sol(0, 0)

    print(f'#{tc} {ans - s}')