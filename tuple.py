# 리스트 < 튜플 : 속도
# 리스트 , 튜플, 딕셔너리, 셋
# p.72 / 85 / 88/ 97
# 리스트 vs 튜플 : 수정 가능 vs 불가능
# 튜플의 선언

t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

# 튜플의 값을 수정, 삭제할때 (p.86)
t6 = (1, 2, 'a', 'b')
print(t2)
# 튜플 수정 --> 리스트 변경-->조작 -->튜플
# print(t7)
# t7 = list(t1)
# t7[0] = 99

print(t3[0:2])

print(t3+t5)

print(t3 * 3)

print('튜플 t5 길이 : ', len(t5))

empty=[]
for i in range(10):
    empty.append(i)