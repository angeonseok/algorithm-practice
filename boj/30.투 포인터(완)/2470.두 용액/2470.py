import sys
input = sys.stdin.readline

n = int(input())
ph = sorted(list(map(int, input().split())))    #정렬을 해놔

r = n -1
l = 0

min_sum = float('inf')      #초기화용

ans = (ph[l], ph[r])    #값 저장용

#값의 합이 0과 가깝도록 조정
while l < r:
    s = ph[l] + ph[r]
    
    if s == 0:
        ans = (ph[l], ph[r])
        break

    elif abs(s) < min_sum:
        min_sum = abs(s)
        ans = (ph[l], ph[r])

    elif s < 0 :
        l += 1
    
    else:
        r -= 1

print(*ans)