import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

#11869와 풀이가 동일. 스프라그-그런디 정리를 알아보자.
ans = 0
for i in nums:
    ans ^= i

if ans == 0:
    print('cubelover')
else:
    print('koosaga')