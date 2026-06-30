import sys
input = sys.stdin.readline

#개행문자 생각안하냐?
s = input().strip()
boom = input().strip()

#스택으로 일단 담자
stack = []
for i in s:
    stack.append(i)

    #스택의 길이가 폭탄 문자열의 보다 크거나 같아지면 
    if len(stack) >= len(boom):
        
        #join으로 문자열 뒤에서부터 boom 길이만큼 꺼내서 합친게 폭탄이면
        if "".join(stack[-len(boom):]) == boom:
            
            #문자열 길이만큼 뺴
            for _ in range(len(boom)):
                stack.pop()
                
if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))