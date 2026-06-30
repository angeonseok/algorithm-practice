import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

counter = Counter(n_list)       #카운터로 딕셔너리 만들자

for i in m_list:
    print(counter[i], end=" ")