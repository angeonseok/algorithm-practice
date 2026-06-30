while 1 :                                           # 0 0 0 전까지 반복
    len_tri = list(map(int,input().split()))

    len_tri.sort()  #길이 정렬해두는게 편해보여서 함

    if len_tri[0] == len_tri[1] == len_tri[2] == 0 :
        break
    elif len_tri[2] >= len_tri[0] + len_tri[1] :
        print('Invalid')
    elif len_tri[0] == len_tri[1] == len_tri[2]:
        print('Equilateral')
    elif len_tri[0] == len_tri[1] or len_tri[1] == len_tri[2] or len_tri[0] == len_tri[2] :
        print('Isosceles')
    else:
        print('Scalene')