T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    #역순으로 정렬해서
    arr.sort(reverse=True)

    #3의 배수 가격 안내면 끝임
    ans = sum(arr[i] for i in range(n) if i % 3 != 2)
    print(f'#{tc} {ans}')