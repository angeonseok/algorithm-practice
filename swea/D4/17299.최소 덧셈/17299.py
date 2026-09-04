T = int(input())
for tc in range(1, T+1):
    nums = input().strip()

    ans = float('inf')

    #흠....
    for i in range(1, len(nums)):
        total = int(nums[:i]) + int(nums[i:])
        ans = min(total, ans)

    print(f'#{tc} {ans}')