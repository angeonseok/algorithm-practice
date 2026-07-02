t = int(input())
ans = []

def gcd(a, b):              #유클리드 호제법 gcd(a,b) = gcd(b, a mod b)
    while b:
        a, b = b, a % b
    return a              

for _ in range(t):
    a, b = map(int,input().split())
    c = int(a * b / gcd(a, b))
    ans.append(c)

for x in ans:
    print(x)