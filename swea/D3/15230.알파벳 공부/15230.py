alpha = "abcdefghijklmnopqrstuvwxyz"

T = int(input())
for tc in range(1, T+1):
    text = input().rstrip()

    ans = 0
    for i in range(len(text)):
        if text[i] == alpha[i]:
            ans += 1
        else:
            break
    
    print(f'#{tc} {ans}')