# p.130 while 문
# 제어문 > 반복문 > while, for (다른 언어 do while)

'''
while 조건문:
    반복 수행할 문장1
    반복 수행할 문장2
    .....문장.....

'''
'''
i = 1
while i <= 10:
    print(f"안녕하세요, {i} 번째 고객님")
    i += 1

num_sum = 0
i = 1
while i <= 10:
    num_sum += i
    print(i)
    i += 1
print("1~10까지 숫자의 총합 : ",num_sum)
'''

#j = 1
#i,j,k,l,m
#dan = int(input('몇단을 알고 싶으신가요?'))
#sum_dan = 0
#while j < 10:
#    print(f"{dan} X {j} = {dan*j}")
#    sum_dan += dan * j
#    j += 1
#print(f'{dan}의 합 : {sum_dan:,}')
# Q 구구단의 합을 구하여, 반복문 끝나면 출력

#  while 반복문으로 * 출력하기
'''
*
**
***
****
*****
'''
i = 1
while i <= 5:
    print('*'*i)
    i += 1
while i>0:
    print('*'*i)
    i -= 1