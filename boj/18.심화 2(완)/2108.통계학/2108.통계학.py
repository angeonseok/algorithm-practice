import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

print(round(sum(arr) / n))

arr.sort()
print(arr[int((n-1)/2)])

#이거 쓰면 틀릴 수 있다는데, Counter 잘 써서 깔끔하게 해결하도록
mode = Counter(arr).most_common()

if len(mode) > 1:
    if mode[0][1] == mode[1][1]:
        print(mode[1][0])
    else:
        print(mode[0][0])
else:
    print(mode[0][0])

print(arr[-1] - arr[0])