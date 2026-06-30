import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int,input().split()))

def cut(arr, length):
    cnt = 0
    for i in arr:
        
        #나무가 설정 높이보다 더 길다면
        if i > length:

            #그 차이만큼 가져간다
            cnt += (i - length)
    
    #가져간 나무 길이가 원하는 길이 이상이면 트루
    if cnt >= m:
        return True
    return False

l, h = 0, max(tree)
ans = -1

#랜선 자르기와 동일
while l <= h:
    mid = (l + h) // 2
    if cut(tree, mid):
        ans = mid
        l = mid + 1
    else:
        h = mid - 1

print(ans)