def check(arr):
    #열마다 검사할거임
    for i in range(w):
        cnt = 1

        #이전꺼랑 현재랑 같으면 카운팅, 아니면 1로 초기화
        for j in range(1, d):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt = 1

            #연달아서 k개 되면 그 열은 검사 끝
            if cnt == k:
                break

        #for문에서 못나옴 = 조건 만족을 못함
        else:
            return False

    #아무일 없으면 조건 전부 만족한 것
    return True


#마구 돌리자
def inject(cur, cnt):
    global ans 

    #가지치기
    if cnt > ans:
        return

    #조건 만족한 경우 횟수 비교
    if check(arr):
        ans = min(ans, cnt)
        return

    #모든 행을 확인하면 ㅌㅌ
    if cur == d:
        return

    #1. 약품투여 안함.
    inject(cur + 1, cnt)

    #약품 투여하는 경우 2가지
    tmp = arr[cur][:]

    #2. A약품 투여
    arr[cur] = [0] * w
    inject(cur + 1, cnt + 1)

    #3. B약품 투여
    arr[cur] = [1] * w
    inject(cur + 1, cnt + 1)

    arr[cur] = tmp


T = int(input())
for tc in range(1, T+1):
    d, w, k = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(d)]

    ans = d

    #처음부터 조건 만족되는 경우 있음
    if check(arr):
        ans = 0
    else:
        inject(0, 0)

    print(f'#{tc} {ans}')