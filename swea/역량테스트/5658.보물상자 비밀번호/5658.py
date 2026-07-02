#파이썬 덱은 신이고 무적이다
from collections import deque

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())

    #돌릴거임
    nums = deque(input().strip())
    
    #사각형 한 변에 들은 놈이 암호
    side = n // 4

    #중복 제거하면서 받을 예정
    created_nums = set()

    for _ in range(side):
        #덱은 슬라이싱 안됨 > 리스트로 ㅇㅇ
        arr = list(nums)

        #한 변에 있는 친구들 묶어서 16진수 변환 > 저장
        for i in range(0, n, side):
            side_num = int(''.join(arr[i:i+side]), 16)
            created_nums.add(side_num)

        #오른쪽으로 1칸 회전
        nums.rotate(1)
    
    #정렬을 위해 리스트로 변환
    created_nums = list(created_nums)
    created_nums.sort()
    
    #k번째로 큰 수 바로 뽑기
    print(f"#{tc} {created_nums[-k]}")