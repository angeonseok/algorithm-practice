import sys
input = sys.stdin.readline

n = int(input())

#좌표가 반시계방향으로 제공됨
point = []
for _ in range(n):
    x, y = map(int,input().split())
    point.append((x,y))
point.append(point[0])      #계산 쉽게할라고 추가

#신발끈 공식
a, b =0, 0
for i in range(n):
    a += point[i][0] * point[i+1][1]
    b += point[i+1][0] * point[i][1]

print(abs(a-b) * 0.5)