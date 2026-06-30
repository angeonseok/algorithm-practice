arr = [ 
    'ABC',  #2 3초     
    'DEF',  #3 4초
    'GHI',  #4 5초
    'JKL',  #5 6초
    'MNO',  #6 7초
    'PQRS', #7 8초
    'TUV',  #8 9초
    'WXZY'  #9 10초
]

a = input()
b = 0

for c in a :                        #input 단어들마다 돌림
    for i in arr :                  #arr 기반 범위 설정
        if c in i :                 #arr 안에 입력문자 있으면
            b += arr.index(i) + 3   #인덱스가 0부터 시작 > 실제 걸리는 시간에 맞게 보정

print(b)