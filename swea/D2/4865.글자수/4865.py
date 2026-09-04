from collections import defaultdict

T = int(input())
for tc in range(1, T+1):
    s1 = set(input().strip())
    s2 = input().strip()

    cnt = defaultdict(int)
    for i in s2:
        if i in s1:
            cnt[i] += 1

    print(f'#{tc} {max(cnt.values(), default=0)}')