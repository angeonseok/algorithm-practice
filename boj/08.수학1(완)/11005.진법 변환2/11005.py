import sys

n, b = map(int, sys.stdin.readline().split())
digit='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ' #진법 변환표
ans = ""

while n != 0:
    ans = digit[n % b] + ans       # n%b 반복해서 나머지 역순하면 진법변환
    n //= b                        # 근데 저렇게 합치면 역순 안해도 됨             

print(ans)