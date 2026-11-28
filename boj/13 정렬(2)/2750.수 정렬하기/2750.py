a = int(input())        #입력 받고
c = []

for i in range(a):      #입력만큼 다시 순차적으로 입력하고 그거 리스트에 박고
    b = int(input())     
    c.append(b)         #정렬하고

c.sort()

for i in range(len(c)) :    #그걸 그냥 순서대로 꺼내서 출력하면 되는거아님?
    print(c[i])