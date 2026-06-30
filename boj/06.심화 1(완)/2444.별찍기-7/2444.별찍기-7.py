n = int(input())

for i in range(1, n+1) :            #범위 조심(1열~n열)
    print((" " * (n - i)) + ('*' * (2*i-1)))    

for i in range(n-1,0,-1) :          #역순으로 따지면 n-1~1 순
    print((" " * (n - i)) + ("*" * (2*i-1)))