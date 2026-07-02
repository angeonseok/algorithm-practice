import sys
sys.setrecursionlimit(100001)   #n 최대 100000이라 이래잡음
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

#처음에 인자 3개로 했다가 망함
def preorder(post_start, post_end, in_start, in_end):
    
    #구간 없으면 끝
    if in_start > in_end or post_start > post_end:
        return
    
    #postorder 맨 끝이 루트
    root = postorder[post_end]

    #inorder 루트 찾기
    mid = in_start
    while mid <= in_end and inorder[mid] != root:
        mid += 1

    #왼쪽 서브트리 크기
    left_size = mid - in_start
    
    #전위순회
    ans.append(root)

    #각 서브트리 루트노드 위치는 저래 나오던데
    preorder(post_start, post_start + left_size - 1, in_start, mid - 1)
    preorder(post_start + left_size, post_end - 1 , mid + 1, in_end)

ans = []
preorder(0, len(postorder) - 1, 0, len(inorder)-1)
print(*ans)