import sys
input = sys.stdin.readline


s = input()
sub_list = []

#모든 부분 문자열 케이스 생성
for i in range(len(s)):
    for j in range(i+1,len(s)):
        sub_list.append(s[i:j])

#중복은 set으로 지우고 개수 세기
print(len(set(sub_list)))