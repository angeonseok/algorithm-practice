import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())

site = defaultdict()

for i in range(n):
    a, b = input().split()
    site[a] = b

for j in range(m):
    com = input().rstrip()
    print(site[com])