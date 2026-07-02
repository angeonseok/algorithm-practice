a = int(input())

def fac(i):
    if i == 0:
        return 1
    else :
        return i * fac(i-1)

b = fac(a)
print(int(b))
        
        

