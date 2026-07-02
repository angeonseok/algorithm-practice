def fac(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    
    return str(result)

n = int(input())
num = fac(n)

cnt = 0
for i in reversed(num):
    if i == "0":
        cnt += 1
    else:
        break

print(cnt)