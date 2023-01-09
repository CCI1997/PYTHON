# 입력
A, B = input().split()

A = int(A[::-1]) 
B = int(B[::-1])

# 출력
if A > B : 
    print(A)
else :
    print(B)
