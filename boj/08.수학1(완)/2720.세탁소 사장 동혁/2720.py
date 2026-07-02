import sys
m = [25, 10, 5, 1]      #100배할랜다

t = int(sys.stdin.readline())
c = [int(sys.stdin.readline()) for _ in range(t)]   

ans = []
for i in c:                 #입력받은 수들 꺼내서
    for j in m:             #리스트 맨 앞놈부터 나눈 몫 카운트하고
        ans.append(i // j)  #카운트 모으고
        i %= j              #카운트한 금액만큼 빼가야겠지

print(*ans)                 #언패킹함