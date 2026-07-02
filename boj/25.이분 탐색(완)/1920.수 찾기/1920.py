def b_s(arr, v):
    l = 0
    r = len(arr) - 1

    #계속 중앙값을 찾아

    while l <= r:
        m = (l + r) // 2        
        if arr[m] == v:
            return 1
        
        elif arr[m] > v:
            r = m - 1
        else:
            l = m + 1
    return 0

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()    #탐색 전에 정렬해야함

for i in range(m):
    print(b_s(a, b[i]))