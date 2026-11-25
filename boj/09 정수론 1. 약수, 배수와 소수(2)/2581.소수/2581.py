m = int(input())
n = int(input())

b = []
p = []

for i in range(m, n+1):
    b.clear()               #매번 초기화해야지
    
    for j in range(1,(int(i ** 0.5) + 1)) : #root i 까지만 범위를 줄이자. n까지 다 하면 너무 걸린다
        if i % j == 0 :
            b.append(j)                     #일단 포함을 시키고
            other = i // j                  #그에 맞는 약수 쌍도 
            if other != j :                 #포함을 시켜야지
                b.append(other)
    
    if len(b) == 2:         #약수 개수가 2개면 > 소수
        p.append(i)         #소수끼리 모아놔

if len(p) == 0:
    print(-1)
else :
    print(sum(p))
    print(p[0])