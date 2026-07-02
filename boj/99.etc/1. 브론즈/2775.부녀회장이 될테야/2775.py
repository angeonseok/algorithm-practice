T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())

    arr = [i for i in range(1, n + 1)] 
    for _ in range(k):
        for i in range(1, n):
            arr[i] += arr[i - 1]

    print(arr[-1])