MOD = 1000000007

#클래스가 아닌 함수로 정의함
#곱셈 결과들은 전부 MOD로 나눠줌
def build(arr, node, start, end):
    if start == end:
        tree[node] = arr[start] % MOD
    else:
        mid = (start + end) // 2
        build(arr, node * 2, start, mid)
        build(arr, node * 2 + 1, mid + 1, end)
        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % MOD

def update(node, start, end, idx, val):
    if start == end:
        tree[node] = val % MOD
    else:
        mid = (start + end) // 2
        if idx <= mid:
            update(node * 2, start, mid, idx, val)
        else:
            update(node * 2 + 1, mid + 1, end, idx, val)
        tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % MOD

def query(node, start, end, left, right):
    if right < start or end < left:
        return 1
    
    if left <= start and end <= right:
        return tree[node] % MOD
    
    mid = (start + end) // 2
    return (query(node * 2, start, mid, left, right) * query(node * 2 + 1, mid + 1, end, left, right)) % MOD

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
N = len(arr)
tree = [0] * (4 * N)
build(arr, 1, 0, N-1)

for _ in range(m + k):
    cmd, b, c = map(int, input().split())

    if cmd == 1:
        update(1, 0, N-1, b-1, c)
        
    elif cmd == 2:
        mul_num = query(1, 0, N-1, b - 1, c - 1)
        print(mul_num)