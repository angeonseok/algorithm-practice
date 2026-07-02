T = int(input())
for tc in range(1, T+1):
    n = int(input())

    speed = 0
    dist = 0

    for _ in range(n):
        cmd = list(map(int, input().split()))

        #커맨드의 존재에 따라 속도를 추가하던가 말던가 하고 이동거리 추가
        if cmd[0] == 1:
            speed += cmd[1]
        
        elif cmd[0] == 2:
            speed -= cmd[1]
            
            if speed < 0:
                speed = 0
        
        dist += speed
    
    print(f"#{tc} {dist}")