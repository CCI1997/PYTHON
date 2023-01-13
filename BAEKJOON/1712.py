# 입력
A, B, C = map(int, input().split())

# 출력
if B >= C:
    print(-1)
else:
    print(int(A / (C - B) + 1))
