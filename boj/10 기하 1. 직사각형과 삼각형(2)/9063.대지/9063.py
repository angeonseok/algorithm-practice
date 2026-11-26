x_1 = []    #x축 정보
y_1 = []    #y축 정보

x_2 = 0     #최종 x값
y_2 = 0     #최종 y값

n = int(input())

for _ in range(n):                         #입력받은거 따로 모으기
    x, y = map(int,input().split())
    x_1.append(x)
    y_1.append(y)

x_2 = max(x_1) - min(x_1)           #x축 길이 = 최대x - 최소x
y_2 = max(y_1) - min(y_1)           #여기도

print(x_2 * y_2)        #땅은 사각형이다