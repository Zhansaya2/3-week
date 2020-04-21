n = int(input())
m = 1
s = 0
while m != n + 1:
    s += 1 / (m ** 2)
    m += 1
print(round(s, 6))
