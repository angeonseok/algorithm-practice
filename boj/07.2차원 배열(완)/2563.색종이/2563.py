a = []
for _ in range(100):
    a.append([0] * 100)    #100x100 색종이 / [[0]*100] *100 이거 안된다

n = int(input())
cnt = 0

for _ in range(n):                      
    x, y = map(int, input().split())
    for i in range(y, y+10):             #색종이 안에 범위 잡고
        for j in range(x, x+10):        #거길 다 1로 칠할 예정
            if a[i][j] == 0 :           #range 순서 바꿔도 결과 안바뀔듯
                a[i][j] = 1
            else :
                pass

for i in range(100):            #다 더해
    for j in range(100):
        cnt += a[i][j]

print(cnt)