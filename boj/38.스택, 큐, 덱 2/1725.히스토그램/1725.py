import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

stack = []
ans = 0


for i in range(n):
    #현재 막대의 시작지점임
    start = i

    #현재 막대보다 더 큰 놈들은 넓이 계산하고 끝내
    while stack and stack[-1][1] > arr[i]:
        a, value = stack.pop()

        # 지금 높이는 더 낮은 놈
        # 방금 뽑은 막대 시작점까지 먹고 들어갈 수 있음
        start = a
        ans = max(ans, value * (i - start))

    #시작지점이랑 높이 같이 넣기
    stack.append((start, arr[i]))

#계산 안된 위치들 전부 계산하기
#맨 오른쪽에서 막대까지 거리를 밑변으로 잡으면 됨
while stack:
    start, value = stack.pop()
    ans = max(ans, value * (n - start))

print(ans)