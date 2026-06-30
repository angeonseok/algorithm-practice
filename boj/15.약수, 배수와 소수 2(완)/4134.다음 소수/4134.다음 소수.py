import sys

def is_prime(m):                        #소수 판별 함수
    if m == 0 or m == 1:                
        return False
    
    for i in range(2,int(m ** 0.5)+1):  # root n까지만 하는 모습
        if m % i == 0:
            return False
        
    return True


t = int(sys.stdin.readline().rstrip())
p = []

for i in range(t):
    num = int(sys.stdin.readline().rstrip())


    while 1:                    #입력받은 num값을 소수가 될 때 까지 반복 상승

        if is_prime(num):
            p.append(num)       #소수되면 모아
            break
        else :
            num +=1

for i in p:                     #답 모아서 출력
    print(i)