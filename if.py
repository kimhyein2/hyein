'''
타 프로그래밍 언어 vs 파이썬
----------------------------
if(조건식){            if 조건식:
...실행코드...          ...실행코드
} else{
...
}
'''

# money = '1'
# if money:
#     print("택시를 타고간다")
# else:
#     print('걸어간다.')
#
# num1 = 4
# num2 = 3
# if num1>num2:
#     print(f'{num1}은 {num2}보다 크다')
#
# '''숫자를 하나 입력받고, 이숫자가 홀수/짝수 여부를 판단하고 내용을 출력하는 조건문을 작성해 봅시다'''
#
# # input_num= input('숫자를 하나 입력하세요') -->문자열 받음
# # int() : 숫자형으로 변환 (castig, 캐스팅 - 형변환)
# # 홀수 : 1,3,5,7,,,
# # 짝수 : 2,4,6,7,,,
#
# input_num = input('숫자를 하나 입력해보세요. ')
# input_num = int(input_num)
# if input_num % 2 == 0:
#     print(f'입력한 숫자 {input_num}은(는) 짝수 입니다.')
# else:
#     print(f'입력한 숫자 {input_num}은(는) 홀수입니다.')

input_num2 = input('숫자를 입력하세요')
last_char = input_num2[-1]
print(last_char)
if last_char in '02468':
    print('짝수를 입력했습니다.')
if last_char in '13579':
    print('홀수를 입력했습니다.')