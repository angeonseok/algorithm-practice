a, b = map(int,input().split())         #2개 받고
c = list(map(int, input().split()))     #리스트도 만들고        
print(sorted(c[-b]))                    #정렬하고 젤 큰 놈부터 세면 된다