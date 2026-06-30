T = int(input())
for tc in range(1, T+1):
    a, code = input().split()

    ans = ""
    for i in code:
        
        #입력문자를 16진수로 쓴다 > 그걸 다시 4자리 2진수로 변경한다. > 문자열에 다 합친다
        ans += format(int(i, 16), "04b")

    print(f"#{tc} {ans}")