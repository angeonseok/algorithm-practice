#매번 계산할 필요 없이 미리 수열만들기
arr = [0] * 1001
arr[0] = arr[1] = 1

for i in range(2, 1001):
    v = 1
    while 1:
        k = 1
        ok = True

        #현재 k 값에서 조건 만족 확인
        while i >= 2 * k:
            if v - arr[i - k] == arr[i - k] - arr[i - 2*k]:
                ok = False
                break

            k += 1

        #모든 k에서 만족한 경우
        if ok:
            arr[i] = v
            break

        v += 1


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    print(arr[n])