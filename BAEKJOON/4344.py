# 입력
C = int(input())

# 출력
for i in range(C):
    num = list(map(int, input().split()))
    avg = sum(num[1:])/num[0]
    cnt = 0
    for i in range(1, len(num)):
        if num[i] > avg:
            cnt += 1
            
    print('%.3f' % (cnt / num[0] * 100) + '%')
