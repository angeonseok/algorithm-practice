x_1 = []    #x축 정보
y_1 = []    #y축 정보

x_2 = 0     #최종 x값
y_2 = 0     #최종 y값

for _ in range(3):                         #입력받은거 따로 모으기
    x, y = map(int,input().split())
    x_1.append(x)
    y_1.append(y)

for i in range(3):                   
    if  x_1.count(x_1[i])== 1:  #사각형이라 좌표 4개면 동일한 값 2개씩
        x_2 = x_1[i]
    
    if y_1.count(y_1[i]) == 1:  #사각형이라 좌표 4개면 동일한 값 2개씩
        y_2 = y_1[i]

print(x_2, y_2)