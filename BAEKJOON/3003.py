# 입력
piece = list(map(int, input().split()))  # 피스

# 리스트
chess = [1, 1, 2, 2, 2, 8]  # 체스

# 출력
for i in range(6):
    print(chess[i] - piece[i], end = ' ')  # 세트
