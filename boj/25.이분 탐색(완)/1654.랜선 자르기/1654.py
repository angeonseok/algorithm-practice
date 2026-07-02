import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input().rstrip()) for _ in range(k)]

# 가능여부 판단
def cut(lan, length):
    
    #갯수 체크용
    cnt = 0

    #랜선들을 주어진 길이만큼 잘랐을 때 몇개의 선이 나오나
    for i in lan:
        cnt += i // length

    #그렇게 자른 선의 수가 요구하는 선의 수보다 많으면 ㅇㅋ
    if cnt >= n:
        return True

    return False

l, h = 1, max(lan)
ans = -1

#이분 탐색 아이디어를 통해 선의 최대 길이 구하기
while l <= h:
    m = (l + h) // 2
    if cut(lan,m):
        ans = m
        l = m + 1
    else:
        h = m - 1

print(ans)