import sys
input = sys.stdin.readline

n = int(input())
tt = [list(map(int, input().split())) for _ in range(n)]

#종료시간 기준 오름차순. 같다면 시작시간 기준 오름차순
tt.sort(key=lambda x : (x[1], x[0]))

cnt = 0

#종료시간 저장용
end = 0

for s, e in tt:
    #종료시간 다음 회의 바로 잡기
    if s >= end:
        cnt += 1
        end = e #잡으면 그에 맞게 종료시간 변동

print(cnt)