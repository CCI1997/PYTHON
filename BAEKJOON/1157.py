# 입력
word = input().upper()

word_list = list(set(word))
cnt = []


for i in word_list:
    cnt.append(word.count(i))

# 출력
if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))])
