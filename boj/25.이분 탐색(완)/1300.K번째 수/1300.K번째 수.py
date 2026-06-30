import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

#답은 최소 1, 최대 k 안에 있음
start = 1
end = k

ans = 0

# mid값을 k번쨰 값의 후보로 본다
while start <= end:
    mid = (start + end) // 2
    cnt = 0

    # i행( i, 2i, 3i, ... , n*i )에서 mid 이하 개수는 mid//i개
    # 근데 한 행에 최대 n개라서 min(mid//i, n)로 자름
    # 모든 행에 대해 mid 이하 원소 개수 카운팅
    for i in range(1, n+1):
        cnt += min(mid // i, n)

    # mid 이하가 k개 이상이면, k번째 값은 mid보다 작거나 같음(왼쪽으로 좁힘)
    if cnt >= k:
        ans = mid
        end = mid - 1

    #그 역의 경우
    else:
        start = mid + 1
        
print(ans)