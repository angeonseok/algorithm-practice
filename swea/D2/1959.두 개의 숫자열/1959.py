T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    if len(arr2) > len(arr1):
        arr1[:], arr2[:] = arr2[:], arr1[:]
    
    ans = 0
    for i in range(len(arr1) - len(arr2) + 1):
        total = 0
        for j in range(len(arr2)):
            total += arr1[j + i] * arr2[j]
        
        ans = max(ans, total)
    
    print(f'#{tc} {ans}')