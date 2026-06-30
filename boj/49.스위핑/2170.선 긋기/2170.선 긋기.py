import sys

def sum_line(arr):
    
    #시작지점 기준으로 정렬
    arr.sort()
    total = 0 
    cur_start, cur_end = arr[0]

    #2개의 구간이 겹치면 합치기
    for start, end in arr[1:]:
        if start <= cur_end:
            cur_end = max(end, cur_end)
        
        #아니라면 한 선분의 길이 합치고, 새 구간 시작
        else:
            total += cur_end - cur_start
            cur_start, cur_end = start, end
    
    #마지막에 남은 선분 길이 합쳐야지
    total += cur_end - cur_start

    return total

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

ans = sum_line(arr)
print(ans)