from itertools import combinations

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    table = [list(map(int, input().split())) for _ in range(n)]

    #combinations 사용하기 위한 밑작업
    food = list(range(n))

    ans = float('inf')
    for t1 in combinations(food, n//2):

        #식재료 반반 나눠서 2그룹으로
        t2 = [i for i in food if i not in t1]

        #식재료의 모든 시너지 값 합치기
        sy1 = 0
        for i in range(n//2):
            for j in range(i + 1, n//2):
                a, b = t1[i], t1[j]
                sy1 += table[a][b]
                sy1 += table[b][a]

        #여기도
        sy2 = 0
        for i in range(n//2):
            for j in range(i + 1, n//2):
                a, b = t2[i], t2[j]
                sy2 += table[a][b]
                sy2 += table[b][a]

        ans = min(ans, abs(sy1 - sy2))

    print(f'#{tc} {ans}')