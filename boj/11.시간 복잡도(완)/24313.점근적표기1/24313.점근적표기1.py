a_1, a_0 = map(int, input().split())
c = int(input())
n_0 = int(input())

#식에 n0 대입, a0이 음수인 경우 a1 =< 이면 무조건 성립
if ((a_1 * n_0) + a_0) <= (c * n_0) and a_1 <= c : 
    print(1)
else:
    print(0)