import sys
input = sys.stdin.readline

n = int(input())
cost = list(map(int,input().split()))
city = list(map(int,input().split()))

#첫 도시에서 무조건 주유하고 가야함
temp = city[0]

ans = 0
for i in range(n-1):
    #일단은 달려
    ans += temp * cost[i]
    
    #현재 도시보다 다음 도시가 가격이 더 싸면 다음 도시에서 주유할거임
    if temp >= city[i+1]:
        temp = city[i+1]

print(ans)