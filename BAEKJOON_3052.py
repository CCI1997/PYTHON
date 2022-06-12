N = []

for i in range(10):
    A = int(input())
    if A % 42 not in N:
        N.append(A % 42)

print(len(N))
