while 1 :                               #계속 입력받는다
    a, b = input().split()  

    if int(a) == 0 and int(b) == 0:     #while 종료조건 : a, b = 0
        break

    if int(a) % int(b) == 0 :           #ㅇㅇ
        print('multiple')
    elif int(b) % int(a) == 0:
        print('factor')
    else:
        print('neither')
    