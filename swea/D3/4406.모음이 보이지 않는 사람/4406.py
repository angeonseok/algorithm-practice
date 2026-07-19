T = int(input())
for tc in range(1, T+1):
    text = input().rstrip()

    ans = ''
    for a in text:
        if a not in "aeiou":
            ans += a
    
    print(f'#{tc} {ans}')