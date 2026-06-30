import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    q = input().strip()

    cnt = 0
    total = 0
    for i in q:
        if i == "O":
            cnt += 1
            total += cnt
        
        else:
            cnt = 0
    
    print(total)