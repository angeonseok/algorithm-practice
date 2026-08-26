def sol(cur, cursum):
    global ans

    #가지치기
    if cursum > k:
        return

    #갯수 체크
    if cursum == k:
        ans += 1
        return

    #맨 마지막 원소까지 갔을 때 종료시켜줘야함
    if cur == n:
        return

    #1. 현재 원소를 선택한 경우
    sol(cur + 1, cursum + arr[cur])

    #2. 현재 원소를 건너 뛴 경우
    sol(cur + 1, cursum)

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    ans = 0
    sol(0, 0)
    print(f'#{tc} {ans}')