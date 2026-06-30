t = int(input())
ans = []

def fac(i):                     #팩토리얼 계산있음
    if i == 0:
        return 1
    else :
        return i * fac(i-1)

for _ in range(t):                  #말만 긴 조합문제
    n, m = map(int, input().split())
    c = str(int(fac(m) / (fac(n) * fac(m-n))))  #소수점 지우고 join쓸라고 
    ans.append(c)

print("\n".join(ans))           #답 한번에 출력