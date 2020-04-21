a = float(input())
b = float(input())
c = float(input())
p = (a + b + c) / 2
S = ((p - a) * (p - b) * (p - c) * p) ** (1 / 2)
if S == int(S):
    print(float(S))
elif S > int(S):
    print(round(S, 6))
