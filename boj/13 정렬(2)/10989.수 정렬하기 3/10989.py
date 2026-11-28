import sys
input = sys.stdin.readline

n = int(input())

cnt = [0] * 10001

for _ in range(n):
    cnt[int(input())] += 1

for i in range(1, 10001):
    if cnt[i]:
        for _ in range(cnt[i]):
            print(i)