'''
if else
'''

a = 11
if a > 10 :
    print('a는 10다 큼!!')
elif a == 10 :
    print('a는 10이다')
else :
    print('a느 10보다 작다')

b = 3.7
if b >= 4.3 :
    print('과탑')
elif 4.3 > b >= 3.7 :
    print('평타')
else :
    print('열심히 살자...')


'''
variable
True = 1
False = 0
'''

if True :
    print('True는 1이다')

if 0 :
    print('0은 False다')

a = 1
if a :
    print('0이 아니다.')
if not a :
    print('0이다.')