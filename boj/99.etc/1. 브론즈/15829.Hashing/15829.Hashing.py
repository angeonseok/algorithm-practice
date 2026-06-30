l = int(input())
arr = input().strip()

mod = 1234567891
ans = 0
for i in range(l):
    ans += ((ord(arr[i]) - 96) * (31 ** i)) % mod

print(ans%mod)