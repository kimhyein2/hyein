#p. 138 for 문
'''
for 변수 in 리스트(튜플, 문자열):
    수행할 코드1
    수행할 코드2
'''
'''
test_list = ['one','two','three']
for i in test_list:
    print(i)
'''
#print(test_list, type(test_list))

# for문을 이용해서 1~10 까지 숫자를 출력
#for i in range(10):
#    print(i+1)

'''
dan = int(input('몇단?'))
gugudan_sum = 0
for i in range(1,10):
    gugudan_sum += i * dan
    print(f'{dan} X {i} = {i*dan}')
print(gugudan_sum)
'''

''' 총 5명의 학생이 시험을 보고, 점수가 60점 넘으면 합격, 그렇지 않으면 불합격을 출력'''

'''
marks = [90, 25, 67, 45, 80]
number = 0
avg = 0
marks_sum = 0
for i in marks:
    number += 1
    marks_sum += i
    if i >= 60:
        print(f'{number}번 학생의 점수는 {i}(으)로 합격입니다.')
    else:
        print(f'{number}번 학생의 점수는 {i}(으)로 불합격 입니다.')
avg = marks_sum / 5
print(f'평균: {avg:.2f}')
'''

# range() - class
# range(정수)
# range(시작값, 마지막값)
# range(시작값, 마지막값, 단계/증가)
# range(시작값, 마지막값, 단계/감소)

for i in reversed(range(1,10,2)):
    print(i, end=" ")