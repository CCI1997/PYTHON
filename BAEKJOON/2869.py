import math

# 입력
A, B, V = map(int, input().split())

day = math.ceil((V - A) / (A - B)) + 1

# 출력
print(day)
