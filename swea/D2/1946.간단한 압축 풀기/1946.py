T = int(input())
for tc in range(1, T+1):
    n = int(input())

    #해독해
    code = ""
    for _ in range(n):
        a, b = map(str, input().split())
        code += a * int(b)
    
    #10개씩 출력해
    print(f"#{tc}")
    for i in range(0, len(code), 10):
        print(code[i:i+10])