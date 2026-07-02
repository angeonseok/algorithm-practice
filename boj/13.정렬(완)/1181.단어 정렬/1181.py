import sys
input = sys.stdin.readline

n = int(input().rstrip())
word = set(input().rstrip() for _ in range(n))  #중복제거

#정렬조건 : 1.길이 2. 오름차순
word = sorted(word,key=lambda x : (len(x), x))

for i in word:
    print(i)