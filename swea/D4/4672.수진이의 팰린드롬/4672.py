from collections import Counter

T = int(input())
for tc in range(1, T+1):
    text = input().strip()

    ans = 0

    #걍 같은 문자 개수마다 자연수의 합 때려서 더하면 되네
    for _, cnt in Counter(text).items():
        ans += cnt * (cnt + 1) // 2

    print(f'#{tc} {ans}')