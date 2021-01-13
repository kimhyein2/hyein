# random 모듈을 이용한 (난수 발생) 임의의 숫자값 맞추기 게임
# 1~10 사이의 난수를 발생, 사용자가 입력(input)한 값과 비교(==)
# 난수를 맞추면, 게임종료 + 맞췄습니다. 아니면 계속 입력하게 하는거
# Q 입력시 즉시 종료

import random, time
start_time = time.perf_counter()
com_input = random.randint(1, 100)
while True:
    userInput = input('1~10사이의 숫자를 입력하세요(게임종료 : Q) ')
    if userInput.upper() == 'Q':
        print('사용자가 게임을 종료했습니다.')
        end_time = time.perf_counter()
        break
    if int(userInput) > com_input:
        print('Down')
    elif int(userInput) < com_input:
        print('Up')
    else:
        print('축하합니다 정답입니다.')
        end_time = time.perf_counter()
        print('-'*50)
        diff_time = end_time - start_time
        print(f'{diff_time:.1f}초 걸렸습니다.')
        print('-'*50)
        break
