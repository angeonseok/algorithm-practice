a = []

for _ in range(5):          #5개 순차적으로 입력받은거 배열로 떄리고
    n = int(input())
    a.append(n)

a.sort()                    #정렬떄리고

print(sum(a) // 5)          #값 5개 평균떄리고
print(a[2])                 #중앙값의 인덱스는 2