n = int(input())
ans = []

for i in range(n) :
    s = sum(map(int,str(i)))       #숫자를 하나의 문자열로 본다면?

    if n == s + i:                 #가장 처음 나온 생성자 바로 출력
        ans = i
        break
    else :
        ans = 0

print(ans)
    