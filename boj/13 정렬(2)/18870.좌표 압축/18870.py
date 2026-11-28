import sys
input = sys.stdin.readline

n = int(input().rstrip())
num = list(map(int, input().split()))

#중복 지우고 정렬을 하자
set_num = sorted(set(num))

#젤 작은 놈부터 0 가진 딕셔너리
dict_num = dict(zip(set_num, range(len(set_num))))  

for i in range(len(num)):
    print(dict_num[num[i]], end=" ")            #ㅇㅇ