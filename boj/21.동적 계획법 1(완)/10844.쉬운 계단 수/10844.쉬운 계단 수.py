import sys
input = sys.stdin.readline

mod = 1000000000
n = int(input())
dp = [0] * (n + 1)

#계단 선택횟수 저장용
s = [0] + [1 for _ in range(9)]
dp[1] = 9

for i in range(2, n+1):

    #이전 계단수와 현재 계단 선택을 분리
    temp = [0] * 10
    
    for j in range(10):
        if j == 0:          #선택지가 1로 가는거 하나
            temp[1] += s[0]
        elif j == 9:        #선택지가 8로 가는거 하나
            temp[8] += s[9]
        else:               #1~8까지는 선택지가 2
            temp[j + 1] += s[j]
            temp[j - 1] += s[j]
    s = temp
    dp[i] = sum(s) % mod    #안나눠서 틀림. 문제를 잘읽자.
print(dp[n])