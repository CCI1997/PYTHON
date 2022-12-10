# 입력
price = int(input())
N = int(input())

# 변수
sum = 0

# 출력
for i in range(N):
    a, b = map(int, input().split())
    sum += a * b

    
if price == sum:
    print('Yes')
else:
    print('No')
