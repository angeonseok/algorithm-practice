T = int(input())
for tc in range(1, T+1):
    a, b = map(int, input().split())
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))

    ans = ""
    if set_a == set_b:
        ans = "="
    elif set_a > set_b:
        ans = ">"
    elif set_a < set_b:
        ans = "<"
    else:
        ans = "?"
    
    print(ans)