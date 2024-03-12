'''
int
'''

print(type(1), type(1.5))

# +, -, *, /, //, %, **

print(1 + 2)
print(1 - 2)
print(1 * 2)

# 나누기
print(10 / 2) # float 로 나오게
print(type(10 / 2)) # float 로 나오게

# 몫
print(10 // 3) # int 로 나오게
print(-99 // 10)

# 나머지
print(99 % 10) # 나머지
print(99 % 2) # 짝수인지 판별

print(-99 % 10) # -1

# 거듭제곱
print(2 ** 3) # 2^3


'''
우선순위
** > * / // % > + -
'''
print(2 + 3 * 4) # 14
print(2 * 3 ** 2) # 18