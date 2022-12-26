# 입력
N = int(input())

# 출력
for i in range(N):
    OX_list = list(input())
    score = 0  
    sum_score = 0  
    for OX in OX_list:
        if OX == 'O':
            score += 1  
            sum_score += score 
        else:
            score = 0
    print(sum_score)
