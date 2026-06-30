a = []
n = 0
result = []                     #문장 모아두기

while n != -1 :                 
    
    n = int(input())
    a.clear()                   #다음 수 입력하면 a 초기화

    if n == -1:                 #ㅇㅇ
        break

    for i in range(1, n+1) :
        if n % i == 0 :                 #약수들 모아둔 배열 만들고.. 
            a.append(i)

    if (sum(a) - a[-1]) != n :                  #문장을 만들고 모으자
        result.append(f'{n} is NOT perfect.')   #눈이 있다면 출력조건을 보자. 2번 틀렸다 이거떄메

    else :          
        line = f'{n} = ' + ' + '.join(map(str,a[:-1]))      #join을 써서 리스트 맨 마지막 항 제외하고 출력
        result.append(line)

print('\n'.join(result))