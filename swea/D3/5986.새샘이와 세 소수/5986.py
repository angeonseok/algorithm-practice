#소수 걸러주기
def make_prime(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False

    #제곱근까지만 하면 됨.
    for i in range(2, int(n ** 0.5) + 1):

        #소수로 판정되면 
        if prime[i]:

            #그 배수는 전부 지워버린다
            for j in range(i * i, n + 1, i):
                prime[j] = False

    return [i for i in range(2, n + 1) if prime[i]]


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    prime = make_prime(n)

    cnt = 0

    #걍 직접 때려박자
    for i in range(len(prime)):

        # x =< y
        for j in range(i, len(prime)):
            z = n - prime[i] - prime[j]

            #y <= z
            if z in prime and z >= prime[j]:
                cnt += 1

    print(f'#{tc} {cnt}')