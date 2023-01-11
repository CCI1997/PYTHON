croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 입력
word = input()

for i in croatia :
    word = word.replace(i, '*')

# 출력
print(len(word))
