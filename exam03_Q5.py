#p.148

stu_score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for i in stu_score:
    total+=i
average = total/10
print(f'총점 : {total}')
print(f'평균 : {average}')
'''
num_a = 10
str_b = 'text'
bool_c = True
bool_d = False

list_e = []
list_f = [1,3,5,7,9]
dic
set
'''

# p.72
# '' 또는 ""로 감싸여져 있으면 -->
# 인덱싱, 슬라이싱 <--> 리스트도 비슷
#
# odd = [1, 3, 5, 7, 9]
# even = [2, 4, 6, 8, 10]
# list_in_list = [1, 2, ['Life', 'is', 'egg']]
# print(odd+even)

# Q6. 리스츠 중에서 홀수에만 2를 곱하여 저장하는 다음의 코드를
# 리스트 내포(list comprehensive)를 이용해 표현해보자
items = [1, 2, 3, 4, 5]

result = []
for item in items:
    if item % 2 == 1:
        result.append(item*2)
print(result)

