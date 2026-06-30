import sys
input = sys.stdin.readline

def gcd(a, b):                          #최대공약수
    while b:
        a, b = b, a % b
    return a

n = int(input().rstrip())
num = [int(input().rstrip()) for _ in range(n)]
num.sort()

m = []
for i in range(len(num)-1):             #각 항의 차 모은 리스트
    k = num[i+1] - num[i]
    m.append(k)

gcd_d = m[0]                            #차의 최대공약수가 공차임
for j in range(1, len(m)):
    gcd_d = gcd(gcd_d, m[j])

cnt = 0
for k in m:                             #카운트 꺠작하니 이리하면 되던데
    cnt += k // gcd_d - 1

print(cnt)