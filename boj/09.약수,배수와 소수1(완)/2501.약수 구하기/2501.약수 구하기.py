a, b = map(int,input().split())     #2개받고
c = []

for i in range(1,a+1) :             #range범위 조심해서 넣고
    if a % i == 0 :                 #약수들 모아둔 배열 만들고
        c.append(i)

if len(c) < b :                     #예외 조건 : 약수의 수 < k => 0
    print(0)
else:                               #인덱스 순서 조심
    print(c[b-1])