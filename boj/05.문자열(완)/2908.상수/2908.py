a, b = input().split()

a_1 = a[::-1]       #a 역순
b_1 = b[::-1]       #b 역순

if a_1 > b_1 :      #대소 비교
    print(a_1)
else :
    print(b_1)