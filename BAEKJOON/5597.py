students = [i for i in range(1,31)]

# 입력
for _ in range(28):
    applied = int(input())
    students.remove(applied)

# 출력
print(min(students))
print(max(students))
