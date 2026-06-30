#누적합 쓰면서 한 아이디어만 챙기자. 이 코드는 문제기준 50점 짜리다.
import sys
input = sys.stdin.readline

text = list(input().rstrip())
q = int(input())

#문자열을 인덱스로 활용하기 위해 사전 작업 및 배치
#이거 안해도 한번에 누적합 생성 가능한데 보기 좋잖아
text_change = [[0] * (len(text)) for _ in range(26)]
for order, ch in enumerate(text):
    text_change[ord(ch)-97][order] += 1

#누적합으로 각 문자의 등장 횟수 저장
prefix = [[0] * (len(text) + 1) for _ in range(26)]
for x in range(26):
    for y in range(1, len(text) + 1):
        prefix[x][y] = text_change[x][y-1] + prefix[x][y-1]

out = []
for _ in range(q):
    a, b, c = map(str, input().split())
    a = ord(a) - 97 
    b = int(b)
    c = int(c) + 1
    out.append(str(prefix[a][c] - prefix[a][b]))

#join으로 한번에 출력
print("\n".join(out))