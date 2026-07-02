import sys
input = sys.stdin.readline

T = int(input())
out = []

for _ in range(T):
    N, K = map(int, input().split())
    
    # 제외되는 내부 크기 (K >= N-1이면 0)
    n2 = max(0, N - 1 - K)          
    out.append(str(2*N*(N+1) - 2*n2*(n2+1)))

print("\n".join(out))