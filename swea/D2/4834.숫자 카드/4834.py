T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = input().strip()
    
    cnt = [0] * 10
    for c in arr:
        cnt[int(c)] += 1
    
    ans_num, ans_cnt = 0, 0
    for i in range(10):
        if cnt[i] >= ans_cnt:
            ans_num, ans_cnt = i, cnt[i]
    
    print(f"#{tc} {ans_num} {ans_cnt}")