import sys
input = sys.stdin.readline

n, m = map(int, input().split())

n_1 = set([input().rstrip() for _ in range(n)])
m_1 = set([input().rstrip() for _ in range(m)])

ans = list(n_1 & m_1)           #set이니까 교집합가자.

ans.sort()                      #출력을 사전순으로 하기 위한 정렬

print(len(ans))
for j in ans:
    print(j)