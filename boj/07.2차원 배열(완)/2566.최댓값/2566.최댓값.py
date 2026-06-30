a = []
max_val = -1        #입력 최소값이 0
max_row = 0         #ㅇㅇ
max_col = 0         #ㅇㅇ

for i in range(9):              #일단 9x9 행렬을 만들어
    i = input().split()
    a.append(i)

for i in range(9):                  #최댓값 찾기는 머
    for j in range(9):
        if max_val < int(a[i][j]) :
            max_val = int(a[i][j])
            max_row = i + 1         #실제 우리가 원하는 값보다 1적음
            max_col = j + 1         #얘도

print(max_val)
print(max_row, max_col)