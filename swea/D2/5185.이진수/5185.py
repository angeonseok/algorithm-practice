T = int(input())
for tc in range(1, T+1):
    a, code = input().split()
 
    ans = ""
    for i in code:
        ans += format(int(i, 16), "04b")
 
    print(f"#{tc} {ans}")