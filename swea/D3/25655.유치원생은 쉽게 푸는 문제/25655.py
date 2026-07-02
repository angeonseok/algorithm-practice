T = int(input())
for tc in range(1, T+1):
    number = int(input())
 
    ans = ""
     
    if number == 1:
        ans = 0
         
    else:
        if number % 2 == 0:
            ans = "8" * (number // 2)
        else:
            ans = "4" + "8" * (number // 2)
     
    print(ans)