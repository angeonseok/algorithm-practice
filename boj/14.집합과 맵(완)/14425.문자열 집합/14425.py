import sys
input = sys.stdin.readline

n, m= map(int,input().split())
n_list = set([input().rstrip() for _ in range(n)])
m_list = [input().rstrip() for _ in range(m)]

cnt = 0                         
for i in m_list:                #흠...
    if i in n_list:
        cnt += 1
print(cnt)