# 입력
T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    people = [i for i in range(1, n + 1)]
    for __ in range(k):
        for j in range(1, n):
            people[j] += people[j - 1]

    # 출력
    print(people[-1])
