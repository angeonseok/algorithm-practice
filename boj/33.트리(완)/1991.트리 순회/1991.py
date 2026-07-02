#부모 > 왼 > 오
def preorder(v):
    if v != ".":
        print(v, end="")
        preorder(tree[v][0])
        preorder(tree[v][1])

#왼 > 부모 > 오
def inorder(v):
    if v != ".":
        inorder(tree[v][0])
        print(v, end = "")
        inorder(tree[v][1])

#왼 > 오 > 부모
def postorder(v):
    if v != ".":
        postorder(tree[v][0])
        postorder(tree[v][1])
        print(v, end = "")

import sys
input = sys.stdin.readline 

n = int(input())

#부모를 키 값으로, 자식을 벨류값으로
tree = {}
for _ in range(n):
    p, l_c, r_c = map(str, input().split())
    tree[p] = l_c, r_c

preorder("A")
print()

inorder("A")
print()

postorder("A")
print()