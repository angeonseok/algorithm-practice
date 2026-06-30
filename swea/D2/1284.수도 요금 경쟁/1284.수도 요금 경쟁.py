T = int(input())
for tc in range(1, T+1):
    p, q, r, s, w = map(int, input().split())

    #a회사는 그대로임
    company_a = p * w
    
    #b회사는 r 까지는 q, 이후는 추가 1L당 s원
    if w <= r:
        company_b = q
    else:
        company_b = q + (w - r) * s

    #둘 중 작은 놈
    print(f"#{tc} {min(company_a, company_b)}")