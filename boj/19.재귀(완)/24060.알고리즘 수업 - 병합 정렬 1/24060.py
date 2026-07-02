import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def merge_sort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge(arr, p, q, r)

def merge(arr, p, q, r):
    global cnt, ans, k

    i, j, t = p, q + 1, 1
    temp = [0] * (r - p + 2)

    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            temp[t] = arr[i]
            t += 1
            i += 1
        else:
            temp[t] = arr[j]
            t += 1
            j += 1

    while i <= q:
        temp[t] = arr[i]
        t += 1
        i += 1

    while j <= r:
        temp[t] = arr[j]
        t += 1
        j += 1

    i = p
    t = 1
    while i <= r:
        arr[i] = temp[t]
        cnt += 1
        if cnt == k:
            ans = arr[i]
        i += 1
        t += 1

n, k = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
ans = -1
merge_sort(arr, 0, n - 1)
print(ans)