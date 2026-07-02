len_3 = list(map(int, input().split()))

len_3.sort()            #정렬하면 확실히 좋음

if len_3[0] + len_3[1] <= len_3[2] :    #젤 긴놈 값만 조정해주면 됨
    len_3[2] = len_3[0] + len_3[1] -1
    print(sum(len_3))
else :
    print(sum(len_3))