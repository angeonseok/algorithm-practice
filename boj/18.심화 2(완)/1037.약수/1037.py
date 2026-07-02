n = int(input())
num = list(map(int,input().split()))        #걍 리스트로 받고

print(max(num) * min(num))                  #정렬해서 젤 큰 놈 젤 작은 놈 곱하면 나오잖아