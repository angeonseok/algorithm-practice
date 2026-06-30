import sys
input = sys.stdin.readline

n = int(input())

#set으로 하니 시간 초과 이슈가 해결된
n_list = set(map(int,input().split()))

m = int(input())
m_list = list(map(int,input().split()))

ans = []     #있으면 1 없으면 0
for i in m_list:
    if i in n_list:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)