s = input().strip()

idx = s.index("*")
total = 0

for i in range(13):
    if s[i] == "*":
        continue

    num = int(s[i])

    if i % 2 == 0:
        total += num
    else:
        total += 3 * num

for j in range(10):
    if idx % 2 == 0:
        temp = total + j
    else:
        temp = total + 3 * j

    if temp % 10 == 0:
        print(j)
        break