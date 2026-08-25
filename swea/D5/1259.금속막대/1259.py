#오 ㅋㅋ
from itertools import chain

def sol(depth, best, used):
    global ans

    #모두 연결 가능한 듯 한데
    if depth == n:
        ans = best[:]
        return True

    #죠뻉이 까야지
    for i in range(n):
        if used[i]:
            continue

        #최근꺼 뒷놈 == 고를 놈 앞놈
        if depth == 0 or best[-1][1] == arr[i][0]:
            used[i] = True
            best.append(arr[i])
            sol(depth+1, best, used)
            best.pop()
            used[i] = False

    return False


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    tmp = list(map(int, input().split()))

    arr = [(tmp[2 * i], tmp[2 * i + 1]) for i in range(n)]

    ans = None
    sol(0, [], [False] * n)
    print(f'#{tc}', end = " ")

    #이런게 있었네
    print(*chain(*ans))