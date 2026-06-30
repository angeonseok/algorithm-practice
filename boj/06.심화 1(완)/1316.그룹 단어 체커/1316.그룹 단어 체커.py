import sys
input = sys.stdin.readline

n = int(input().rstrip())
word = [input().rstrip() for _ in range(n)]

cnt = n
for i in range(n):
    seen = set()                        #이미 문장 내에 있던 글자
    for j in range(1, len(word[i])):
        if word[i][j] != word[i][j-1]:  #글자가 다른데
            if word[i][j] in seen:      #그 글자가 이미 문장내에 있었다?
                cnt -= 1                #넌 나가라
                break
            seen.add(word[i][j-1])      #연속이 끝난 문자 기록
print(cnt)