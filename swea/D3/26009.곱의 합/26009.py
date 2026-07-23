T = int(input())
for tc in range(1, T+1):
    a, b, c = map(int, input().split())

    i = (a * (a + 1) // 2) % 998244353
    j = (b * (b + 1) // 2) % 998244353
    k = (c * (c + 1) // 2) % 998244353
    
    ans = (i * j * k) % 998244353
    print(ans)