T = int(input())
for tc in range(1, T+1):
    weed = input().rstrip()

    ans = 0
    for i in weed:
        if i == '(' or i == ')':
            ans += 1
    
    ans -= weed.count("()")
    print(f'#{tc} {ans}')