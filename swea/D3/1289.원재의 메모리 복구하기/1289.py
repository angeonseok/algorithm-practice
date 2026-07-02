T = int(input())
for tc in range(1, T+1):
    bit = input()   #문자열로 받음
    p = '0'         #변환용. 초기값은 0
    cnt = 0

    for i in range(len(bit)):
        if p != bit[i]:     #현재 비트랑 p가 다르다면
            cnt += 1        #카운팅
            p = bit[i]      #다음 비트값 상태 저장

    print(f'#{tc} {cnt}')