def t_90(arr, n):
    t_arr = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n-1,-1,-1):
            t_arr[i].append(arr[j][i])
    return t_arr

T = int(input())

for a in range(1,T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    
    arr_90 = t_90(arr, n)
    arr_180 = t_90(arr_90, n)
    arr_270 = t_90(arr_180, n)

    print(f'#{a}')
    for i in range(n):
        print("".join(map(str, arr_90[i])),end=" ")
        print("".join(map(str, arr_180[i])),end=" ")
        print("".join(map(str, arr_270[i])),end="\n")