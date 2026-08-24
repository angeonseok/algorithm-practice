def sol(cnt, arr):
    global ans

    if cnt == n:
        ans = max(ans, int("".join(arr)))
        return
    
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]

            #시행횟수별 중복 케이스 가지치기용
            if (cnt, int("".join(arr))) not in visited:
                sol(cnt + 1, arr)
                visited.add((cnt, int("".join(arr))))

            arr[i], arr[j] = arr[j], arr[i]


T = int(input())
for tc in range(1, T+1):
    tmp, tmp_n  = input().split()
    num = list(tmp)
    n = int(tmp_n)

    #가지치기용 set
    visited = set()
    ans = -1
    sol(0, num)

    print(f'#{tc} {ans}')