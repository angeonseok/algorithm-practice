def cut(l):
    a = len(l) // 3
    if len(l) == 1: #길이가 1이 되면 '-' 출력
        return "-"
    
    #계속 중앙 1/3 날려
    else:
        return cut(l[0:a]) + ' ' * a + cut(l[2*a : 3*a])

import sys
input = sys.stdin.readline

#EOF에서 종료되도록
while 1:
    try:
        n = int(input())
        l = '-' * (3 ** n)
        print(cut(l))
    except:
        break