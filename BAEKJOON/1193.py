# 입력
X = int(input())

num_list = []
num = 0
num_count = 0

while num_count < X:
    num += 1
    num_count += num

num_count -= num

if num % 2 == 0:
    i = X - num_count
    j = num - i + 1
else:
    i = num - (X - num_count) + 1
    j = X - num_count

# 출력
print(f"{i}/{j}")
