class SegmentTree:
    def __init__(self,arr):
        self.n = len(arr)

        # 세그트리 배열
        # 보통 넉넉하게 4배 잡음
        self.tree = [0] * (4 * self.n)

        # 1번 노드가 arr 전체 구간 담당하게 시작
        self.build(arr, 1, 0, self.n - 1)

    def build(self, arr, node, start, end):
        # 리프 노드면 걍 원본 값 박기
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2

            # 왼쪽 자식은 [start ~ mid]
            self.build(arr, node * 2, start, mid)

            # 오른쪽 자식은 [mid+1 ~ end]
            self.build(arr, node * 2 + 1, mid + 1, end)

            # 현재 노드는 자식 둘의 합
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def update(self, node, start, end, idx, val):
        # 리프까지 내려왔으면 값 갱신
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2

            # 바꾸려는 idx가 왼쪽 구간에 있으면 왼쪽으로
            if idx <= mid:
                self.update(node * 2, start, mid, idx, val)

            # 아니면 오른쪽으로
            else:
                self.update(node * 2 + 1, mid + 1, end, idx, val)

            # 자식 바뀌었으니까 현재 노드 합도 다시 계산
            self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def query(self, node, start, end, left, right):
        # 아예 안 겹치면 합에 영향 없으니까 0
        if right < start or end < left:
            return 0

        # 현재 구간이 찾는 범위 안에 완전히 들어오면 바로 사용
        if left <= start and end <= right:
            return self.tree[node]

        # 일부만 겹치면 반 갈라서 계속 내려감
        mid = (start + end) // 2
        return self.query(node * 2, start, mid, left, right) + self.query(node * 2 + 1, mid + 1, end, left, right)
    

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

st = SegmentTree(arr)

for _ in range(m + k):
    cmd = list(map(int, input().split()))

    # 1 b c : b번째 수를 c로 바꾸기
    if cmd[0] == 1:
        st.update(1, 0, st.n-1, cmd[1] - 1, cmd[2])
    
    # 2 b c : b ~ c 구간합 출력
    elif cmd[0] == 2:
        sum_num = st.query(1, 0, st.n-1, cmd[1] - 1, cmd[2] - 1)
        print(sum_num)