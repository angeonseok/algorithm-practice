import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = float("inf")

man = list(range(n))

#파이썬의 조합을 이용, 팀 하나를 미리 만든다.
for team1 in combinations(man, n//2): 
    
    #안 뽑힌 애들끼리 팀 만들고
    team2 = []
    for i in man:
        if i not in team1:
            team2.append(i)
    
    #1팀의 시너지 총합 계산
    total_1 = 0
    for i in range(n//2):
        for j in range(i+1, n//2):
            a = team1[i]
            b = team1[j]
            total_1 += arr[a][b] + arr[b][a]
    
    #2팀의 시너지 총합 계산
    total_2 = 0
    for i in range(n//2):
        for j in range(i+1, n//2):
            a = team2[i]
            b = team2[j]
            total_2 += arr[a][b] + arr[b][a]

    #차의 최소를 저장
    ans = min(ans, abs(total_1 - total_2))

print(ans)