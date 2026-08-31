from bisect import bisect_left

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    #lis는 이진탐색으로도 된다
    lis = []

    for i in arr:
        #lis에서 i보다 크거나 같은놈 왼쪽 인덱스 반환한다. 제일 크면 길이를 반환함
        k = bisect_left(lis, i)

        #lis에서 제일 큰 놈이면 집어넣고
        if k == len(lis):
            lis.append(i)

        #아니면 인덱스보고 값 변경하면 됨.
        else:
            lis[k] = i

    #lis 길이 반환하면 됨
    print(f'#{tc} {len(lis)}')