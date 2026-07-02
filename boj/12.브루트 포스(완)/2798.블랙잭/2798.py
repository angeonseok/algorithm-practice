import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
card = list(map(int, sys.stdin.readline().split()))

com = list(combinations(card, 3))           #조합모듈이 있으면 금방하지
ans = 0

for i in com:
    if sum(i) <= m:
        ans = max(ans, sum(i))

print(ans)