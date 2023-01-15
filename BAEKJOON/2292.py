# 입력
N = int(input())

nums, count = 1, 1

while N > nums:
    nums += 6 * count
    count += 1

# 출력
print(count)
