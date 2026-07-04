T = int(input())

for tc in range(1, T+1):
    s = input()

    for i in range(1, 11):
        l = 1
        flag = True

        for l in range(i, 30):
            if s[l] != s[l - i]:
                flag = False
                break
            l += 1
        
        if flag:
            print(f'#{tc} {i}')
            break