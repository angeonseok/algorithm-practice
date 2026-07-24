from collections import deque

T = int(input())
for tc in range(1, T+1):
    text = deque(input().rstrip())
    n = int(input())
    cmd = list(map(int, input().split()))

    for i in cmd:
        text.rotate(-i)

    print("".join(text))