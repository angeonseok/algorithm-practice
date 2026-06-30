import sys
input = sys.stdin.readline

n = int(input().rstrip())
cnt = 0
hello = set()               #유저 중복 제거 후 모아둠

for _ in range(n):
    user = input().rstrip()

    if user == 'ENTER':     #엔터 > 기존 유저 수 카운트 후 유저 초기화
        cnt += len(hello)   #엔터 전까지 유저 수
        hello = set()       #빈 셋으로
    
    else :
        hello.add(user)     #엔터 들어오기 전까지 계속 추가
cnt += len(hello)           #다 돌리고 카운트 이거 뺴먹어서 좀 걸림

print(cnt)