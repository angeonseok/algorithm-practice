a = input().upper()     #일단 입력값을 대문자로 고정시키자
b = list(set(a))        #받은 리스트 안에 요소들이 뭔지 보자
cnt = []

for i in b:                 #단어요소를
    count = a.count(i)      #처음 받은 문장에 몇개 들었나 세고
    cnt.append(count)       #리스트에 모아

if cnt.count(max(cnt)) >= 2:    #최댓값이 여러개면 ?
    print("?")

else:
    most = max(cnt)         #답을 꺼내자
    idx = cnt.index(most)
    ans = b[idx]
    print(ans.upper())