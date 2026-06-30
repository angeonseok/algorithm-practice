#세그먼트 트리인데 업데이트 필요없음
import sys
input = sys.stdin.readline

#최댓값 세그먼트 트리
class MaxSegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 1, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
            return

        mid = (start + end) // 2
        self.build(arr, node * 2, start, mid)
        self.build(arr, node * 2 + 1, mid + 1, end)
        self.tree[node] = max(self.tree[node * 2], self.tree[node * 2 + 1])

    def _query(self, node, start, end, left, right):
        if right < start or end < left:
            return -10**18      #연산에 영향을 주지 않게 

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        return max(
            self._query(node * 2, start, mid, left, right),
            self._query(node * 2 + 1, mid + 1, end, left, right)
        )

    def query(self, left, right):
        return self._query(1, 0, self.n - 1, left, right)

#최소값 세그먼트 트리
class MinSegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 1, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
            return

        mid = (start + end) // 2
        self.build(arr, node * 2, start, mid)
        self.build(arr, node * 2 + 1, mid + 1, end)
        self.tree[node] = min(self.tree[node * 2], self.tree[node * 2 + 1])

    def _query(self, node, start, end, left, right):
        if right < start or end < left:
            return 10**18       #연산에 영향을 주지 않게 

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        return min(
            self._query(node * 2, start, mid, left, right),
            self._query(node * 2 + 1, mid + 1, end, left, right)
        )

    def query(self, left, right):
        return self._query(1, 0, self.n - 1, left, right)


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

st_max = MaxSegmentTree(arr)
st_min = MinSegmentTree(arr)

for _ in range(m):
    a, b = map(int, input().split())
    print(st_min.query(a - 1, b - 1), st_max.query(a - 1, b - 1))