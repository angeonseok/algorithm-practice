#단순 조합문제인줄
#페르마의 소정리 문제였고

MOD = 10**9 + 7

#팩토리얼 결과를 미리 계산해두기
fac = [1] * (2000001)
for i in range(1, len(fac)):
    fac[i] = (i * fac[i-1]) % MOD

#우선 식을 만족하는 a, b 찾기
def find(X, Y):
    a = 2 * Y - X
    b = 2 * X - Y

    if a % 3 != 0 or b % 3 != 0:
        return -1, -1
    
    return a // 3, b // 3
     
#a, b를 이용한 조합 계산
def sol(X, Y):
    a, b = find(X, Y)
    
    #조합 생성 불가능한 a, b 값 나오면 ㅂㅂ
    if a < 0 or b < 0:
        return 0
    
    n = a + b

    #모듈로 역원 곱셈
    return (fac[n] * pow(fac[a] * fac[b], MOD - 2, MOD)) % MOD 

T = int(input())
for tc in range(1, T+1):
    X, Y = map(int, input().split())
    print(f"#{tc} {sol(X, Y)}")