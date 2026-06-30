T = int(input())
for tc in range(1, T+1):
    a = int(input())
    num = a
    k = 1
    
    #계속 곱하면서 각 자리의 숫자 넣기
    #0~9 총 10개들어가면 그때의 a값 출력
    numbers = set()
    while len(numbers) < 10:
        cur = num * k
        for i in str(cur):
            numbers.add(i)
        k += 1

    print(f"#{tc} {cur}")
