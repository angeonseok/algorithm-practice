import sys
input = sys.stdin.readline

n, m = map(int,input().split())

#배열 생성
arr = []
for i in range(n):
    arr.append(input().strip())


#체스판은 8x8 시작점은 최대 n-7,m-7
ans = []
for j in range(n-7):
    for k in range(m-7):
        #b 시작, w 시작 따로
        b = 0
        w = 0

        #8x8 채우는 과정
        for x in range(j, j+8):
            for y in range(k, k+8):
                
                #좌표 기준 잡고 칠하기
                if (x+y) % 2 == 0:
                    # 짝수 칸 B로 칠할 때
                    if arr[x][y] != 'B':
                        b += 1
                    # W로 칠할 때    
                    if arr[x][y] != 'W':
                        w += 1
                else:
                    #홀수칸 잘못 칠해진거도 세야지
                    if arr[x][y] != 'W':
                        b += 1
                    if arr[x][y] != 'B':
                        w += 1
        #케이스 2개 모아서
        ans.append(b)
        ans.append(w)

#더 작은 놈 출력
print(min(ans))