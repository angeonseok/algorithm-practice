T = int(input())
for tc in range(1, T+1):
    text = list(input().rstrip())

    text.sort()

    ans = ""
    if text[0] == text[1] and text[2] == text[3] and text[0] != text[2]:
        ans = "Yes"
    else:
        ans = "No"

    print(f'#{tc} {ans}')