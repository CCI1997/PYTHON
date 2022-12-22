num_list = []

# 입력
for i in range(9):
    num_list.append(int(input()))
    
# 출력
print(max(num_list))
print(num_list.index(max(num_list)) + 1)
