from itertools import combinations, permutations

T = int(input())
for tc in range(1, T+1):
    n = int(input())

    arr = [tuple(map(int, input().split())) for _ in range(n)]

    ans = float('inf')

    #2개씩 짝지을거임. comb안에 있는 놈을 시작점으로 보겠다.
    for comb in combinations(arr, n//2):
        # 어차피 백터부터 만들고 총 합의 거리를 구하니까
        x = y = 0

        #걍 모든 좌표 값들 뺴고
        for i in arr:
            x -= i[0]
            y -= i[1]

        #시작점 걸린 놈들 좌표 보정해서 더하면 그게 벡터 총합 아니겠나
        for j in comb:
            x += 2 * j[0]
            y += 2 * j[1]

        #내 30분
        ans = min(ans, x ** 2 + y ** 2)

    print(f'#{tc} {ans}')