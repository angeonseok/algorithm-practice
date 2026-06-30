import sys
input = sys.stdin.readline

#배열, 설치 개수, 간격으로 해볼 예정
def wifi(arr, m, k):
    #최초 설치 개수
    cnt = 1
    
    #최초 설치 위치
    last = arr[0]

    #배열을 보면서 현재 위치와 설치 위치 차이가 간격보다 크다면
    for i in range(1, len(arr)):
        if arr[i] - last >= k:
            cnt += 1            #그 곳에 공유기를 설치하고               
            last = arr[i]       #설치 위치 업데이트
    
    #현재 간격으로 문제에서 원하는 설치 수가 나온다면 ㅇㅋ
    if cnt >= m:
        return True
    
    return False
    
n, m = map(int, input().split())

arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)

#거리를 정렬해야함
arr.sort()

#설치 간격의 최소와 최대 설정
min_dist = 1
max_dist = arr[0] + arr[-1]

ans = 0

#이분 탐색으로 설치 간격 찾기
while min_dist <= max_dist:
    mid = (min_dist + max_dist) // 2

    if wifi(arr, m, mid):
        ans = mid
        min_dist = mid + 1
    
    else:
        max_dist = mid - 1

print(ans)