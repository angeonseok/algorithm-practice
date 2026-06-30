import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    dic = {}

    #종류별로 세고
    for _ in range(n):
        a, b = map(str, input().split())

        if b in dic:
            dic[b] += 1
        else:
            dic[b] = 1

    ans = 1
    #안끼는 경우까지(+1) 해서 곱하자
    for v in dic.values():
        ans *= (v + 1)

    #전부 안입는 경우 1개 빼
    print(ans - 1)