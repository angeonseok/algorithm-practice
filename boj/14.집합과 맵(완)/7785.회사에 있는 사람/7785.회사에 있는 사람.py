import sys
input = sys.stdin.readline

n = int(input())
log = {}

#딕셔너리로 받자
for _ in range(n):
    name, status = map(str,input().split())

    #enter면 저장, 아니면 지워
    if status == 'enter':
        log[name] = status
    else:
        del log[name]

#key값 기준 내림차순
log = sorted(log.keys(),reverse=True)

for i in log:
    print(i)