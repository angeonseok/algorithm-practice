n = int(input())
num = 0
cnt = 0
ans = 0

while cnt < n:                      #카운트 갯수 맞을 때 까지 뺑이
    num +=1
    if '666' in str(num) :          #"문자"로 보면 되는거 아닌가
        cnt += 1
        ans = num
    
    if cnt == n:
        break

print(ans)
    