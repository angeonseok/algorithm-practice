T = int(input())
for tc in range(1, T + 1):
    num = int(input())
    
    # 2, 3, 5, 7, 11로 나눈 횟수 카운팅
    ans = [0] * 5
    
    #계속 나누면서 나눈 수 카운팅 
    while num != 1:
        if num % 2 == 0:
            ans[0] += 1
            num //= 2
 
        elif num % 3 == 0:
            ans[1] += 1
            num //= 3
 
        elif num % 5 == 0:
            ans[2] += 1
            num //= 5
 
        elif num % 7 == 0:
            ans[3] += 1
            num //= 7
 
        else:
            ans[4] += 1
            num //= 11
 
 
    print(f"#{tc}", *ans)