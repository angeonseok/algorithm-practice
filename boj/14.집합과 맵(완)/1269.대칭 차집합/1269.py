import sys
input = sys.stdin.readline

a, b = map(int, input().split())

a_1 = input().split()
b_1 = input().split()

a_1 = set(a_1)             
b_1 = set(b_1)

c = a_1 - b_1
d = b_1 - a_1

print(len(c) + len(d))