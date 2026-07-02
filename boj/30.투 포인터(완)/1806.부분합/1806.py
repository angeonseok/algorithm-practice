import sys
input = sys.stdin.readline

n,s = map(int, input().split())
arr = list(map(int, input().split()))

#투포인터
r, l = 0, 0
sum_num = 0

#최솟값을 찾아보자
ans = 9876543210

while r < n:
    sum_num += arr[r]
    r += 1

    #만약 구간합이 원하는 값을 넘었다면
    while sum_num >= s:
        ans = min(r - l, ans)   #최소길이를 찾을 때 까지
        sum_num -= arr[l]       #l값을 늘려
        l+= 1

#합을 만족하는 수가 없다면 0을 출력
if ans == 9876543210 :
    print(0)
else:
    print(ans)