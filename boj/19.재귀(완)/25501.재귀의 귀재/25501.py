def recursion(s, l, r):
    global cnt                  #글로벌로 카운트값 유지
    cnt +=1
    if l >= r: 
        return 1                #지가 바꿔놓고 까먹는 사람이 있다?
    elif s[l] != s[r]: 
        return 0
    else: 
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for _ in range(int(input())):
    cnt = 0
    s = input().rstrip()
    print(isPalindrome(s), cnt)