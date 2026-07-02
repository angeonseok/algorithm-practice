a, b = map(int,input().split())

def gcd(a, b):              #유클리드 호제법 gcd(a,b) = gcd(b, a mod b)
    while b:
        a, b = b, a % b
    return a              

print(int(a * b/ gcd(a,b))) #float로 나와서 2번틀림 ㅎ