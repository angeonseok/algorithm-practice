score = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())
for tc in range(1, T + 1):
    n, k = map(int, input().split())

    arr = []
    for i in range(n):
        a, b, c = map(int, input().split())
        arr.append((a, b, c))

        if i == k - 1:
            target = (a, b, c)
    
    arr.sort(key=lambda x: x[0] * 0.35 + x[1] * 0.45 + x[2] * 0.2, reverse=True)

    cut = n // 10
    rank = arr.index(target)
    print(f'#{tc} {score[rank//cut]}')