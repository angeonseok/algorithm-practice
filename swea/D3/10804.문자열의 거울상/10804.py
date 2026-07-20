table = {
    'q' : 'p',
    'p' : 'q',
    'b' : 'd',
    'd' : 'b',

}


T = int(input())
for tc in range(1, T+1):
    text = list(input().rstrip())
    text.reverse()

    ans = ""
    for i in text:
        ans += table[i]
    
    print(f'#{tc} {ans}')