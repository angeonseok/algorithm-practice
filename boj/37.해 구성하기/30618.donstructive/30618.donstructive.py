import sys
input = sys.stdin.readline

n = int(input())

odds = list(range(1, n + 1, 2))       
evens = list(range(2, n + 1, 2))[::-1]  

print(*(odds + evens))