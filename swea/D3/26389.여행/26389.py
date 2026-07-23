T = int(input())
for tc in range(1, T+1):
    dirs = list(set(input().strip()))

    a = dirs.count('N')
    b = dirs.count('S')
    c = dirs.count('E')
    d = dirs.count('W')

    if a - b == 0 and c - d == 0:
        print("Yes")
    else:
        print("No")