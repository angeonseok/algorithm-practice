import sys
input = sys.stdin.readline

def misere(piles):
    xor = 0
    for pile in piles:
        xor ^= pile
    
    #모든 더미 크기가 1인지 확인
    all_one = all(p <= 1 for p in piles)

    if all_one:
        #더미 개수가 홀수면 현재 플레이어 짐
        return sum(piles) % 2 == 0
    
    else:
        #그냥 님게임과 동일
        return xor != 0

n = int(input())
arr = list(map(int, input().split()))

winner = misere(arr)

if winner:
    print('koosaga')
else:
    print('cubelover')