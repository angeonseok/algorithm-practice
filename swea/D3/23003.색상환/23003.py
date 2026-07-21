table_A = {
    "red" : ["purple", "orange"],
    "purple" : ["red", "blue"],
    "blue" : ["purple", "green"],
    "green" : ["blue", "yellow"],
    "yellow" : ["green", "orange"],
    "orange" : ["yellow", "red"],
}


table_C = {
    "red" : "green",
    "purple" : "yellow",
    "blue" : "orange",
    "green" : "red",
    "yellow" : "purple",
    "orange" : "blue",
}

T = int(input())
for tc in range(1, T+1):
    a, b = input().split()

    if a == b:
        print('E')
    elif b in table_A[a]:
        print('A')
    elif b == table_C[a]:
        print('C')
    else:
        print('X')