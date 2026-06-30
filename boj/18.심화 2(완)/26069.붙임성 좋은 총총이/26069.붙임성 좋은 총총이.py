import sys
input = sys.stdin.readline

n = int(input())
dance = {'ChongChong'}          #총총이는 춤을 추고 싶다.중복 제거

for _ in range(n):          
    a, b = input().split()

    if a in dance:              # 입력 받은 두 사람 중
        dance.add(b)            # 한 명이 춤을 춘다면
    if b in dance:              # 반대 쪽 애도 춤추겠지
        dance.add(a)

print(len(dance))