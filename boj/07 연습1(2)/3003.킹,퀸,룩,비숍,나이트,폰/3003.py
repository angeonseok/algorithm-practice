a = list(map(int, input().split())) #킹 퀸 룩 비숍 나이트 폰 갯수 입력
b = [1, 1, 2, 2, 2, 8]      #실제 말의 갯수

for i in range(6):             #걍 리스트 2개 만들어서 빼면 되는거 아님?
    print(b[i] - a[i], end=" ")