a = int(input())
b = int(input())
c = int(input())

if a + b + c != 180 :           #조건 맞추면 끝
    print('Error')
elif a == b == c == 60 :
    print('Equilateral')
elif a == b or b == c or c == a :
    print('Isosceles')
else:
    print('Scalene')