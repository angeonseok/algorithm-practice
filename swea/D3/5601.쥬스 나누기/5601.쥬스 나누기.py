T = int(input())
for tc in range(1, T+1):
    n = int(input())
    
    ans = "1" + "/" + str(n)
    print(f"#{tc}",end= " ")
    for _ in range(n):
        print(ans,end=" ")
    print()