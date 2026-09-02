#itertools 하면 그냥 끝나는데 치매노인 되는거같아서 직접 조합 구현
def comb(cur, total, cnt):
    if cnt == 3:
        combs.add(total)
        return

    if cur == 7:
        return

    comb(cur + 1, total + nums[cur], cnt + 1)
    comb(cur + 1, total, cnt)


T = int(input())
for tc in range(1, T+1):
    nums = list(map(int, input().split()))

    combs = set() 
    comb(0, 0, 0)

    #어떻게든 정렬해서 알아서 하십쇼
    combs = sorted(combs)

    print(f'#{tc} {combs[-5]}')