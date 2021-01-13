# p.144리스트 내포(list comprehensive)
# java 배열 == python 리스트

a = [1, 2, 3, 4]
#result = [num*3 for num in a]
print('a의 형태', type(a))
print(len('안녕하세요'))
print('a의 길이', len(a))

# for num in a:
#     result.append(num*3)
#print('result : ',result)
import random # 난수 발생하는 방법 1. 난수 발생 모듈 설치
# 랜덤모듈(난수 발생) - 파이참, 가상환경(venv)
random_list = []
# .append() : 배열에 값을 추가하는 명령어
# 반복문을 다룰줄 안다 : while, for
for i in range(10):
    rand_num = random_list.append(random.randint(1,10))

print(random_list)