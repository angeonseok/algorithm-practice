a = int(input())       #테스트 케이스 개수

for _ in range(a) : 
    r, s = input().split() #r회 s = 문자
    for x in s:
        print(x * int(r),end="") #글자마자 s회 따닥따닥 붙여서
    print()             #줄넘김