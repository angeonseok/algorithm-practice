T = int(input())
for tc in range(1, T+1):
    n = int(input())

    #입력 왜이래
    arr = []
    while len(arr) < n:
        arr.extend(input().split())

    #하나의 문자열로 볼거다
    text_arr = "".join(arr)

    ans = 0
    
    #숫자 존재도 count 이용해서 존재여부 확인할거다.
    while text_arr.count(str(ans)):
        ans += 1

    print(f'#{tc} {ans}')