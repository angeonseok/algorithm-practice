import sys
import math
input = sys.stdin.readline

n = int(input())

man = list(map(int, input().split()))
t, p = map(int, input().split())

ans_t = 0
for i in man:
    ans_t += math.ceil(i / t)

p1 = n // p
p2 = n % p

print(ans_t)
print(p1, p2)