words = ["ZRO", "ONE", "TWO", "THR", "FOR",
         "FIV", "SIX", "SVN", "EGT", "NIN"]

# "ZRO" : 0, ~~~~~
value = {w : i for i, w in enumerate(words)}

T = int(input())
for tc in range(1, T+1):
    input()
    arr = input().split()

    #갯수 카운팅
    cnt = [0] * 10
    for w in arr:
        cnt[value[w]] += 1

    #0부터 카운팅해서 문자 복사
    result = []
    for i in range(10):
        result.extend([words[i]] * cnt[i])

    print(f'#{tc}', " ".join(result))