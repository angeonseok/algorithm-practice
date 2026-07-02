T = int(input())

for _ in range(T):
    x1,y1,r1,x2,y2,r2 = map(int,input().split())

    
    l = (((x2-x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

    #무수히 많은 교점
    if l == 0 and r1 == r2:
        print(-1)

    #교점 2개
    elif abs(r1 - r2) < l < r1 + r2:
        print(2)
    
    #교점 1개
    elif l == r1 + r2 or l == abs(r1 - r2):
        print(1)
    
    else:
        print(0)