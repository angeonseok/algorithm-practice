base_table ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

T = int(input())
for tc in range(1, T+1):
    s = input()

    binary = ""
    for i in s:
        #테이블에 저장된 문자의 인덱스를 구하고, 그것을 6자리 이진수로 변환
        binary += format(base_table.find(i), '06b')

    ans = ""
    for k in range(0, len(binary), 8):
        #8개씩 잘라서 만든 8자리 이진수를 10진법으로 변환한 후, 문자로 변환
        ans += chr(int(binary[k:k+8], 2))

    print(f"#{tc} {ans}")