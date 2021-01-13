import datetime

now_date = datetime.datetime.now()
# print(now_date)
# AM, PM
print(now_date.year)
print(now_date.month)
print(now_date.day)
print(now_date.hour)
print(now_date.minute)

now_hour = now_date.hour
if now_hour > 12:
    print(f'현재는 PM {now_hour-12}시 입니다.')
else:
    print(f'현재는 AM{now_hour}시 입니다.')