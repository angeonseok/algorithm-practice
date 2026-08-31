T = int(input())
for tc in range(1, T+1):
    dna1 = input().strip()
    dna2 = input().strip()

    n = len(dna1)
    m = len(dna2)

    #그냥 lcs문제임
    lcs = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dna1[i - 1] == dna2[j - 1]:
                lcs[i][j] = lcs[i - 1][j - 1] + 1

            else:
                lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])

    print(f'#{tc} {lcs[n][m]}')