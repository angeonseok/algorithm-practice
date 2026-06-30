import sys
input = sys.stdin.readline

n = int(input())

#돈 빨리 뽑는 놈부터 앞에 세워야 최소
line = sorted(list(map(int,input().split())))

sum = 0
time = 0
for i in range(n):
    time += line[i]     #누적시간 계산
    sum += time
print(sum)