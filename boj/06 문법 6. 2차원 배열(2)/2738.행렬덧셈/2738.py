n, m = map(int,input().split())

a = []                      #이러면 행렬 하나
for i in range(n) :
    i = input().split()
    a.append(i)

b = []                      #이러면 행렬 또 하나
for j in range(n) :
    j = input().split()
    b.append(j)

for i in range(n) :                 #행렬 합치기
    for j in range(m):
        print(int(a[i][j]) + int(b[i][j]), end=" ")
    print()
