import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temp = list(map(int, input().split()))

#일단 누적합 생성
prefix = [0] * (n + 1)
for i in range(1, n + 1):
    prefix[i] = prefix[i-1] + temp[i-1]  

#누적합 간의 차를 이용. 걍 이중 for 뇌빼고 돌렸다 터짐.
sub = [0] * (n - k + 1)
for i in range(n-k+1):
    sub[i] = prefix[i+k] - prefix[i]

print(max(sub))