# p.102 불 자료형
# 불, 불리언 / bool, boolean
# True, False vs 참, 거짓

# 명시적인 표현
is_true = True
is_false = False

# 비교 연산자 : >, >=, <, <=, ==, !=
# 논리 연산자 : and, or, not
# print(4>5)

print(type(is_true))
print(1==1)
print(1 is 1)

# 불린 값 True : 실행함
# 불린 값 False : 실행하지 않음
# '' or "" - 공백문자
# [],{},()- 리스트,튜플,딕셔너리 (=원소나 값이 없는 상태)
# None , 0

#p.104
a = [1, 2, 3, 4]
print(type(a))
while a:
    print(a.pop())
    print(a)

# 변수=초기값
# while 조건문(식):
#   수행할 문장(코드)
#   변수의 증감식

print("안" in "안녕하세요")