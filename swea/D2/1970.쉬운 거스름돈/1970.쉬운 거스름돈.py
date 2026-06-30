money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())
for tc in range(1, T+1):
    a = int(input())
    cnt = [0] * 8

    for i in range(8):
        cnt[i] = a // money[i]
        a %= money[i]
    
    print(f"#{tc}")
    print(*cnt)