a = []

for _ in range(5):              #입력을 받아
    a.append(input())       

for i in range(15):                 #최대글자수
    for j in range(5):              #최대문장수    
        if i < len(a[j]):           #문장 길이보다 i가 더 크면 안돌아간다 
            print(a[j][i], end="") 
