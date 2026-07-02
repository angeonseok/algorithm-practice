import sys
input = sys.stdin.readline

n = int(input())

def tower(n, start, end, aux):

    #원판 남은거 1개면 끝내
    if n == 1:
        return print(start, end)

    #1. 위에 n-1개를 end를 보조축으로 start > aux로 이동
    tower(n-1, start, aux, end)

    #2. 가장 큰 원판을 start > end로 이동
    print(start,end)

    #3. aux에 모아둔 n-1개를 end로 모아서 마무리
    tower(n-1, aux, end, start)

#총 이동횟수는 2^n - 1
print(2**n - 1)
tower(n, 1, 3, 2)