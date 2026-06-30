import sys
input = sys.stdin.readline

n, m = map(int,input().split())

#이름 > 번호 , 번호 > 이름
dict_pokemon_name = {}
dict_pokemon_number = {}

for i in range(1, n+1):
    a = input().rstrip()
    dict_pokemon_name[a] = i
    dict_pokemon_number[i] = a

#입력이 숫자인가? 문자인가?
for j in range(m):
    b = input().rstrip()
    if b.isdecimal():
        print(dict_pokemon_number[int(b)])
    else:
        print(dict_pokemon_name[b])