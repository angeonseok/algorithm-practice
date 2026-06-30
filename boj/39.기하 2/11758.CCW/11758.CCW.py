import sys
input = sys.stdin.readline

point = []
x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())

#이차원 외적으로 방향 판단
cross = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

if cross == 0:
    print(0)
elif cross < 0:
    print(-1)
else:
    print(1)