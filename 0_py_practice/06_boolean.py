'''
Boolean
'''
print(type(True), type(False))


print(+True) # 1
print(+False) # 0


a = 1
b = 2
print(a == b) # False


'''
Boolean 연산자
'''

print(True * 2) # 2
print(False * 2) # 0
print(10 // True) # 10

print(True and True) # True
print(True and False) # False
print(True or False) # True
print(False or False) # False


# not
print(not True) # False
print(not False) # True

print(not 1 == 1) # False


'''
비교 연산자
==, !=, >, <, >=, <=
'''

print(1 == 1) # True
print(1 != 1) # False
print(1 > 1) # False
print(1 < 1) # False
print(1 >= 1) # True
print(1 <= 1) # True

print('abc' > 'bcd') # False 사전순으로 비교 (a < b) -> 빠른걸 더 작은 것으로 판단