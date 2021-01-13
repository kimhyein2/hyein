#49. 문자열 연산하기
'''
숫자연산자 : +, -, *, /. %, **, //
'''
head = 'python'
tail = 'is fun'
print(head+tail)

a= 'python'
print('='*50)
print(a*10)
print(10*a)

# len() : 문자열의 길이를 구하는 함수

# 인덱싱 : 몇번째 문자(열)을 가리키는 것
print(len(head))
#print() 줄바꿈기능이 있기 때문에, end=''를 쓰면 줄바꿈X
print(head[0], end='')
print(head[1], end='')
print(head[2], end='')
print(head[3], end='')
print(head[4], end='')
print(head[5])
# 슬라이싱 잘라내는 것
# string_a = "Life is too short, you need Python"
# print(string_a.upper()) #모두 대문자로
# print(string_a.lower()) #모두 소문자로

#p.53 / 슬라이싱 : 잘라내는것
string_a = "LIFE IS TOO SHORT, YOU NEED PYTHON"
string_b = "life is too short, you need python"
string_c = string_a[0]+string_a[1]+string_a[2]+string_a[3]
print(string_c)
print(string_a[0:4])
print(string_a[-6:])
print(string_a[28:])
print(string_a[0:8:2]) #[시작:끝:단계]