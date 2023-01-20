# 입력
N = int(input())

count = 0

# 출력
while N >= 0:
  if N % 5 == 0:
    count += int(N // 5)
    print(count)
    break
  N -= 3
  count += 1
else:
  print(-1)
