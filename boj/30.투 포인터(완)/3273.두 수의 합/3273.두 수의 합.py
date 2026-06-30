#변수명을 바꿨으면 좀 바꾸자
import sys
input = sys.stdin.readline

n = int(input())
lst = sorted(list(map(int, input().split())))   #정렬하고 시작
k = int(input())

#양 끝 포인터 설정
cnt = 0
l = 0
r = n -1

#양 끝에서 중앙으로
while r > l:
    s = lst[r] + lst[l]
    if s == k:
        cnt += 1
        r -= 1
        l += 1

    #크게 더한 쪽을 줄여야지
    elif s > k:
        r -= 1
    
    #작게 더한 쪽을 늘려야지
    else:
        l += 1

print(cnt)