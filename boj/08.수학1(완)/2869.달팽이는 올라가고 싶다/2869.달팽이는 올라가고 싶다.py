a, b, v = map(int,input().split())

# v-a의 걸이를 하루에 a - b 만큼 올라가면 됨
i = 1 + (v - a) // (a - b)

#근데 저 계산식 일수에 나머지가 있으면 올림처리해야됨
if (v - a) % (a - b) != 0:  
    i += 1

print(i)

