T = int(input())
for tc in range(1, T+1):
    n, m ,k = map(int, input().split())
    lst = sorted(list(map(int, input().split())))   #도착 시간 정렬

    bread = 0
    ans = 'Possible'
    
    #시간의 흐름 따라 생각해보자
    for i in range(max(lst) + 1):   #젤 늦은 놈이 올 때 까지
        
        #시간이 m초가 되면 빵 갯수 추가
        if i and i % m == 0 :
            bread += k
        #m초 후 사람이 오면 빵 -1
        if i in lst:
            bread -= 1
        
        #빵이 음수가 되는 순간 바로 빵을 못주니까 끝내
        if bread < 0 :
            ans = 'Impossible'
            break
        
    print(f'#{tc} {ans}')