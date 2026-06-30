import sys
input = sys.stdin.readline

n = int(input())

#소수생성
def prime(n):
    p = [True] * (n + 1)
    p[0] = False
    p[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if p[i] : 
            for j in range(i * i, n + 1, i):
                p[j] = False
    
    return p

#대응되는 수로 전환
arr = prime(n)
prime_list = []
for i in range(len(arr)):
    if arr[i]:
        prime_list.append(i)

l, r = 0, 0
sum_num = 0
cnt = 0

while r < len(prime_list):

    #부분합을 이용
    sum_num += prime_list[r]
    r += 1

    while sum_num > n :
        sum_num -= prime_list[l]
        l += 1

    #소수합이 주어진 수와 같으면 카운팅
    if sum_num == n:
        cnt += 1

print(cnt)