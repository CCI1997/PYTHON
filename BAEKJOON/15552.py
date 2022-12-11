# 모듈
import sys

# 입력
T = int(input())

# 출력
for i in range(T):
        A, B = map(int, sys.stdin.readline().split())
        print(A + B)
