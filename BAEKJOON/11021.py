# 입력
T = int(input())

# 출력
for i in range(1, T + 1):
    A, B = map(int, input().split())
    print(f'Case #{i}: {A + B}')
