import sys
from itertools import combinations
from bisect import bisect_right     # 이분탐색 날먹용
input = sys.stdin.readline

n, c = map(int, input().split())

arr = list(map(int, input().split()))
k = len(arr) // 2

# 전체가 최대 2^30이라서 반으로 쪼개서 부분합 따로 구함
# 나중에 두 리스트에서 합쳐서 c 이하인 경우의 수 계산
l = arr[:k]
r = arr[k:]

l_subset_sum = []
r_subset_sum = []

# 가능한 부분집합 합 전부 넣기
for i in range(len(l) + 1):
    for j in combinations(l, i):
        l_subset_sum.append(sum(j))

for i in range(len(r) + 1):
    for j in combinations(r, i):
        r_subset_sum.append(sum(j))

# 오른쪽은 이분탐색하려고 정렬
r_subset_sum.sort()

cnt = 0
for x in l_subset_sum:

    # bisect_right : 정렬된 배열에서 값을 넣을 수 있는 가장 오른쪽 위치
    # 여기서는 오른쪽 부분합 중 c - x 이하인 개수 세는 용도
    cnt += bisect_right(r_subset_sum, c - x)

print(cnt)