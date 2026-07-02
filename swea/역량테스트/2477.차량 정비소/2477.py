T = int(input())
for tc in range(1, T + 1):
    N, M, K, A, B = map(int, input().split())
    a_time = list(map(int, input().split()))
    b_time = list(map(int, input().split()))
    arrive = list(map(int, input().split()))

    # 접수 창구 상태: [고객번호, 남은시간]
    rec = [[0, 0] for _ in range(N)]

    # 정비 창구 상태: [고객번호, 남은시간]
    rep = [[0, 0] for _ in range(M)]

    # 접수 기다리는 고객
    wait_rec = []
    for i in range(K):
        wait_rec.append([arrive[i], i + 1])   # [도착시간, 고객번호]

    # 정비 기다리는 고객
    wait_rep = []   # [접수끝난시각, 접수창구번호, 고객번호]

    # 고객이 사용한 창구 번호 기록
    used_rec = [0] * (K + 1)
    used_rep = [0] * (K + 1)

    done = 0
    time = 0

    while done < K:
        # 1. 정비 끝난 사람 처리
        for i in range(M):
            if rep[i][0] != 0 and rep[i][1] == 0:
                done += 1
                rep[i][0] = 0

        # 2. 접수 끝난 사람 -> 정비 대기열
        for i in range(N):
            if rec[i][0] != 0 and rec[i][1] == 0:
                cid = rec[i][0]
                wait_rep.append([time, i + 1, cid])   # 끝난 시각, 접수창구번호, 고객번호
                rec[i][0] = 0

        # 3. 정비 창구 배정
        wait_rep.sort(key=lambda x: (x[0], x[1]))   # 접수 끝난 시각 빠른 순, 접수 창구 번호 작은 순
        idx = 0
        for i in range(M):
            if rep[i][0] == 0 and idx < len(wait_rep):
                finish_time, rec_num, cid = wait_rep[idx]
                rep[i] = [cid, b_time[i]]
                used_rep[cid] = i + 1
                idx += 1
        wait_rep = wait_rep[idx:]

        # 4. 접수 창구 배정
        arrived_now = []
        remain_wait = []

        for t, cid in wait_rec:
            if t <= time:
                arrived_now.append(cid)
            else:
                remain_wait.append([t, cid])

        wait_rec = remain_wait
        arrived_now.sort()

        idx = 0
        for i in range(N):
            if rec[i][0] == 0 and idx < len(arrived_now):
                cid = arrived_now[idx]
                rec[i] = [cid, a_time[i]]
                used_rec[cid] = i + 1
                idx += 1

        # 아직 못 들어간 사람은 다시 대기
        for j in range(idx, len(arrived_now)):
            wait_rec.insert(0, [time, arrived_now[j]])

        # 5. 시간 1초 진행
        for i in range(N):
            if rec[i][0] != 0:
                rec[i][1] -= 1

        for i in range(M):
            if rep[i][0] != 0:
                rep[i][1] -= 1

        time += 1

    ans = 0
    for cid in range(1, K + 1):
        if used_rec[cid] == A and used_rep[cid] == B:
            ans += cid

    if ans == 0:
        ans = -1

    print(f'#{tc} {ans}')