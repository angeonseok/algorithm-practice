import sys

m,n = map(int,sys.stdin.readline().split())

def is_prime(n):                        #에라토스테네스의 체
    p = [True] * (n + 1)                #1978, 11653에서도 도움 받았다.
    p[0] = False
    p[1] = False

    for i in range(2, int(n**0.5)+1):
        if p[i] :
            for j in range(i * i, n + 1, i):
                p[j] = False
    pm = [i for i in range(2, n + 1) if p[i]]

    return pm

a = is_prime(n)

for i in a :
    if i >= m:
        print(i)