n = int(input())

if n == 0:
    print(0)
else:
    arr = [int(input()) for _ in range(n)]
    arr.sort()

    #파이썬 올림을 믿지말자
    #0.5 더하고 내림해
    cut = int(n * 0.15 + 0.5)

    cut_arr = arr[cut:n-cut]
    ans = sum(cut_arr) / len(cut_arr)

    print(int(ans + 0.5))