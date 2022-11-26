# 입력
A = int(input())
B = int(input())

# 출력
print(A * (B % 10))
print(A * ((B % 100) // 10))
print(A * (B // 100))
print(A * B)
