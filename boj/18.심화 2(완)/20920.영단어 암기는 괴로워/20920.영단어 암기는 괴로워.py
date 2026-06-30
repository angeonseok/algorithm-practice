import sys
input = sys.stdin.readline
from collections import Counter

n, m = map(int, input().split())

#입력 받을 때 걸러
word = []
for i in range(n):
    w = input().rstrip()
    if len(w) >= m:
        word.append(w)

#카운터쓰면 카운팅 + 중복제거
word_c = Counter(word)

#딕셔너리 형태라 key 뽑아오고
word = list(word_c.keys())

#1. 빈도수 높은 순 2. 길이가 긴 거 3. 사전 순
word.sort(key = lambda x : (-word_c[x], -len(x), x))

for i in word:
    print(i)