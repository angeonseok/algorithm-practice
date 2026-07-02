T = int(input())
for tc in range(1, T+1):
    s = input()
    r_s = s[::-1]

    if s == r_s:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")