A, B = map(int, input().split()) # A는 시, B는 분
C = int(input()) # C는 시간(분 단위)

time_h = C // 60
time_m = C % 60

A += time_h
B += time_m

if B >= 60:
    A += 1
    B -= 60

if A >= 24:
    A -= 24

print(A, B)
