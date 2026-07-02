def fib(n):
    global f1
    if n == 1 or n == 2:
        f1 += 1
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibb(n):
    global f2
    f = [0] * (n+1)
    f[1] = 1
    f[2] = 1

    for i in range(3, n+1):
        f[i] = f[i-1] + f[i-2]
        f2 += 1

    return f[n]

n = int(input())

f1, f2 = 0, 0
fib(n)
fibb(n)
print(f1, f2)