import sys
input = sys.stdin.readline

n, q = map(int, input().split())
sets = [set() for _ in range(n+1)]  #처음에 뭔 소린지 몰랐다. 집합을 만들자

for i in range(1, n + 1):
    arr = list(map(int, input().split()))

    for j in arr[1:]:
        sets[i].add(j)

for i in range(q):
    cmd = list(map(int, input().split()))

    #출력을 먼저 했네
    if cmd[0] == 2:
        print(len(sets[cmd[1]]))
    
    else:
        a = cmd[1]
        b = cmd[2]

        #유니온 파인드 랭크기준 합치기처럼
        #실제 집합의 크기 기준으로 큰 놈에 작은 놈을 합쳤네
        #합치고 작은 쪽은 공집합으로 만들었네
        if len(sets[a]) < len(sets[b]):
            sets[a], sets[b] = sets[b], sets[a]
        
        sets[a].update(sets[b])
        sets[b].clear()