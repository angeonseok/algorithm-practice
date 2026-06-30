from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    synergy = [list(map(int, input().split())) for _ in range(n)]

    food = list(range(n))
    ans = 10**18

    for f1 in combinations(food, n//2):
        f2 = []
        for i in food:
            if i not in f1:
                f2.append(i)

        f1_synergy = 0
        for i in range(n//2):
            for j in range(i+1, n//2):
                a = f1[i]
                b = f1[j]
                f1_synergy += synergy[a][b] + synergy[b][a]
        
        f2_synergy = 0
        for i in range(n//2):
            for j in range(i+1, n//2):
                a = f2[i]
                b = f2[j]
                f2_synergy += synergy[a][b] + synergy[b][a]

        ans = min(ans, abs(f1_synergy - f2_synergy))

    print(f"#{tc} {ans}")