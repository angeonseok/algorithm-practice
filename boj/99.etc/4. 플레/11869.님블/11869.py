import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

#걍 xor만 하면 끝나네. 근데 설명을 못하겠다.
ans = 0
for i in nums:
    ans ^= i

if ans == 0:
    print('cubelover')
else:
    print('koosaga')