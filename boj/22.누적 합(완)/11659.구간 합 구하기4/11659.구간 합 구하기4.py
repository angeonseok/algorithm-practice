import sys
input = sys.stdin.readline

n, m = map(int,input().split())
lst = list(map(int, input().split()))

#인덱스 조정
prefix = [0] * (n+1)
for i in range(1, n+1):
    prefix[i] = lst[i-1] + prefix[i-1]  #0 5 9 12 14 15

#계산
for _ in range(m):
    i, j = map(int,input().split())
    print(prefix[j] - prefix[i-1])