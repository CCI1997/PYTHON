# 입력
N = int(input())
M = list(map(int, input().split()))

max_score = max(M)

for i in range(N):
    M[i] = M[i] / max_score * 100

# 출력
print((sum(M) / N))
