#코드 다 짜놓고 눈물만 줄줄 흘린 문제
import sys

#10**6 이러니 터짐. 걍 노드 수 + 1로 하니까 되네
sys.setrecursionlimit(10001)

#처음엔 try~except로 받았는데 sys.stdin.read()로 한번에 받을 수 있다네
preorder = list(map(int, sys.stdin.read().split()))

#출력도 한번에 모아서 할 예정
ans = []

# 처음엔 리스트 잘라서 넘겼다가 메모리 터짐
# 그래서 구간 인덱스만 넘김
def postorder(start, end):
    if start > end:
        return 
    
    # preorder[start]가 현재 서브트리 루트
    mid = start + 1
    
    #이진 검색 트리 특성상 루트보다 작으면 전부 왼쪽
    while mid <= end and preorder[mid] < preorder[start]:
        mid += 1

    #후위순회이므로 왼 > 오 > 루트
    postorder(start + 1, mid - 1)
    postorder(mid, end)
    ans.append(preorder[start])

postorder(0, len(preorder)-1)
print('\n'.join(map(str, ans)))