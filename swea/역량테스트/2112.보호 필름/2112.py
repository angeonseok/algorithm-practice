#1. 체크를 한다.
def check():
    for i in range(w):
        cnt = 1
        for j in range(1, d):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt = 1

            if cnt >= k:
                break
        
        #k개 미만이라 False 반환
        else:
            return False
    
    #전부 다 돌면 True
    return True


#2. 약품 투여를 한다.
def inject(row, cnt):
    global ans

    #가지치기    
    if cnt >= ans:
        return
    
    #성능검사 통과하면 정답 갱신
    if check():
        ans = min(ans, cnt)
    if row == d:
        return 
    
    cur_row = arr[row][:]

    #1. 걍 간다
    inject(row+1, cnt)

    #2. A 투여한다
    arr[row] = [0] * w
    inject(row+1, cnt+1)

    #3. B 투여한다
    arr[row] = [1] * w
    inject(row+1, cnt+1)

    arr[row] = cur_row 


T = int(input())
for tc in range(1, T + 1):
    d, w, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(d)]

    ans = d
    
    if check():
        ans = 0
    
    else:
        inject(0,0)

    print(f"#{tc} {ans}")