T = int(input())
for tc in range(1, T+1):
    n = input()
    arr = list(map(int, input().split()))

    #빈도 체크용 배열
    max_arr = max(arr)
    cnt = [0] * (max_arr + 1)

    #체크하고
    for i in arr:
        cnt[i] += 1
    
    #실제 최빈값을 모아서
    temp = []
    max_cnt = max(cnt)
    for i in range(len(cnt)):
        if cnt[i] == max_cnt:
            temp.append(i)

    #최빈값들 중 가장 큰 수 출력
    temp.sort()
    print(f"#{tc} {temp[-1]}")