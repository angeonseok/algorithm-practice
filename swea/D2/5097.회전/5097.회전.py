T = int(input())

#실제로 회전 안시키고 바로 구할 수 있음.
for tc in range(1, T+1):
    n, m = map(int, input().split())
    num = list(map(int,input().split()))
    
    print(f'#{tc} {num[m % n]}')