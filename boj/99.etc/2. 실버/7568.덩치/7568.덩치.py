import sys
input = sys.stdin.readline

n = int(input())
man = [list(map(int, input().split())) for _ in range(n)]

ans = []
for i in range(n):
    w, h = man[i]   #자신을 기준으로
    cnt = 1

    #자기보다 더 큰 놈이 있으면 등수 밀림
    for j in range(n):
        if w < man[j][0] and h < man[j][1]:
            cnt += 1
    ans.append(cnt)

print(*ans)