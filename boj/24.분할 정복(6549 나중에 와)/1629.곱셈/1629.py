#숫자 크게 곱하면 터져서 매 계산마다 나눔
def mul_mod(a, b, c):
    if b == 0:
        return 1 % c
    
    #C^n = C^(n/2) * C^(n/2)
    if b % 2 == 0:
        n_b = mul_mod(a, b // 2, c)
        return (n_b * n_b) % c
    
    #C^n = C^(n/2) * C^(n/2) * C
    else:
        n_b = mul_mod(a, (b-1) // 2, c)
        return ((n_b * n_b) % c) * a % c
    
import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
print(mul_mod(a, b, c))