import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

#정답을 담을 리스트
ans = []
for x in arr:

    # x가 ans에서 어디 들어가나 보자
    temp = bisect_left(ans, x)

    #ans 끝에 들어가야 되면 길이 늘어나는거라 추가
    if temp >= len(ans):
        ans.append(x)

    #아니면 기존값 갱신
    else:
        ans[temp] = x

print(len(ans))