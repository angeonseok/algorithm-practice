#정답의 결과 != 실제 역추적 결과

import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

#이분 탐색 lis는 금방인데
#그 값이 있던 인덱스도 저장해야 역추적하지
#근데 그냥 저장만 한 배열만 있으면 역추적에서 막히던데
#그래서 값 저장 + 인덱스 저장 이후 이전 인덱스 저장을 따로 처리했네

ans = []            #길이별 최소 끝값
trace = []          #그 끝값이 들어있는 실제 인덱스
prev = [-1] * n     #현재 인덱스 오기 직전 인덱스

for i, x in enumerate(arr):
    temp = bisect_left(ans,x)
    
    if len(ans) <= temp:
        ans.append(x)
        trace.append(i)
    else:
        ans[temp] = x
        trace[temp] = i
    
    if temp > 0:
        prev[i] = trace[temp - 1]

result = []
cur = trace[-1]
while cur != -1:
    result.append(arr[cur])
    cur = prev[cur]

print(len(ans))
print(*reversed(result))