a, b = map(int,input().split())
c, d = map(int,input().split())

def gcd(a, b):              #유클리드 호제법 gcd(a,b) = gcd(b, a mod b)
    while b:
        a, b = b, a % b
    return a

e = a * d + b * c           #이 문제가 실버 3? 기약분수 만들거면 분모 분자 최대공약수로 나누면 끝이잖
f = b * d

g = int(e / gcd(e, f))
h = int(f / gcd(e, f))

print(g, h)