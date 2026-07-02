T = int(input())

for t in range(1, T+1):
    X, Y = map(int, input().split())
    
    a = (X + Y) // 2
    b = X - a

    print(a, b)