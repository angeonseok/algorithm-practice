x, y, w, h = map(int, input().split())

k = [w-x, h-y, x, y]    #경계선까지 가는 경로 4개
print(min(k))           #그 중 젤 짧은 놈