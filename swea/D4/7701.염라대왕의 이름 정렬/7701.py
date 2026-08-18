T = int(input())
for tc in range(1, T+1):
    n = int(input())

    #중복 제거
    arr = set()
    for i in range(n):
        arr.add(input().strip())

    #람다 조건 아냐?
    arr = sorted(arr, key=lambda x : (len(x), x))

    print(f'#{tc}')
    for w in arr:
        print(w)