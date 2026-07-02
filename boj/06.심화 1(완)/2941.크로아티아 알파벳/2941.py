import sys
input = sys.stdin.readline

a = input().rstrip()        # \n까지 들어오는거 잊지마라
b = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']   #크로아티아 알파벳 모음

for i in b:                 #1157이랑 비슷한 아이디어
    a = a.replace(i, '*')   #1글자짜리 문자로 아무렇게 변경

print(len(a))               #총 개수는 문자열 길이지
