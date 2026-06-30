T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    rus = [input().strip() for _ in range(n)]

    ans = 2501

    #3구간으로 나눠서 완전 탐색
    for i in range(n-2):
        for j in range(i+1, n-1):
            cnt = 0

            for a in range(i + 1):
                cnt += m - rus[a].count('W')

            for b in range(i + 1, j + 1):
                cnt += m - rus[b].count('B')
            
            for c in range(j + 1, n):
                cnt += m - rus[c].count('R')

            if cnt < ans:
                ans = cnt

    print(f'#{tc} {ans}')