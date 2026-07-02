x = int(input())

#1라인 : 1/1, 2라인:(1/2 2/1) 3라인:(3/1 2/2 1/3)...... 
line = 0                       
line_end = 0                    #라인의 끝이 몇번쨰냐

while line_end < x :            #line_end가 x보다 커지는 순간 끝
    line += 1
    line_end += line

    k = line_end - x            #line_end 기준 x가 몇칸 떨어졌는가.
    
    if line % 2 == 0:           #line이 양수냐 음수냐에 따라 a,b가 바뀜
        a = line - k            #노트에 써봄
        b = 1 + k               #노트에 써봄
    else :
        a = 1 + k
        b = line - k

print(str(a) + "/" + str(b))