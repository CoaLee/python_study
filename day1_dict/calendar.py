print('하랑 프터디 달력 프로그램')

year = int(input('년: '))
month = int(input('월: '))
day = int(input('일: '))

# 1. 입력 받아서 출력하기  (print, input, variable, operation)
print('입력한 날은: {}년 {}월 {}일 입니다.'.format(year, month, day))


# 2. 윤달 계산  (if, elif, else, and/or)
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    is_yoon = True
else:
    is_yoon = False

''' hard
if month == 2:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_yoon = True
            else:
                is_yoon = False
            is_yoon = False
        else:
            is_yoon = True
    else:
        is_yoon = False
'''
if is_yoon:
    print('{}년은 윤달이 있는 해입니다.'.format(year))
else:
    print('{}년은 윤달이 없는 해입니다.'.format(year))


# 3. month_days 계산
if month == 2:
    if is_yoon:
        month_days = 29
    else:
        month_days = 28
elif month in [1, 3, 5, 7, 8, 10, 12]:
    month_days = 31
elif month in [4, 6, 9, 11]:
    month_days = 30
else:
    print('월 입력이 잘못됐습니다.')

''' hard coding
if month == 1:
    month_days = 31
elif month == 2:
    if is_yoon:
        month_days = 29
    else:
        month_days = 28
elif month == 3:
    month_days = 31
elif month == 4:
    month_days = 30
elif month == 5:
    month_days = 31
elif month == 6:
    month_days = 30
elif month == 7:
    month_days = 31
elif month == 8:
    month_days = 31
elif month == 9:
    month_days = 30
elif month == 10:
    month_days = 31
elif month == 11:
    month_days = 30
elif month == 12:
    month_days = 31
else:
    print('월 입력이 잘못됐습니다.')
'''

print('{}월은 {}일까지 있는 달입니다.'.format(month, month_days))
if day < 1 or day > month_days:
    print('일 입력이 잘못됐습니다.')


# 4. 이번 달 마지막 날과 1일은 무슨 요일인지 구하기
diff_last = (month_days - 24) % 7
if diff_last == 0:
    weekday_string = '화'
elif diff_last == 1:
    weekday_string = '수'
elif diff_last == 2:
    weekday_string = '목'
elif diff_last == 3:
    weekday_string = '금'
elif diff_last == 4:
    weekday_string = '토'
elif diff_last == 5:
    weekday_string = '일'
elif diff_last == 6:
    weekday_string = '월'
print('9월 {}일은 {}요일입니다'.format(month_days, weekday_last))

diff_first = (1 - 24) % 7
if diff_first == 0:
    weekday_string = '화'
elif diff_first == 1:
    weekday_string = '수'
elif diff_first == 2:
    weekday_string = '목'
elif diff_first == 3:
    weekday_string = '금'
elif diff_first == 4:
    weekday_string = '토'
elif diff_first == 5:
    weekday_string = '일'
elif diff_first == 6:
    weekday_string = '월'
print('9월 {}일은 {}요일입니다'.format(1, weekday_first))


# 6. 이번 달 날짜 입력 받아서 요일 출력하기
target_day = int(input('2019년 9월 몇 일? '))
diff_target = (target_day - 24) % 7
weekday_list = ['화', '수', '목', '금', '토', '일', '월']
print('9월 {}일은 {}요일입니다'.format(target_day, weekday_list[diff_target]))


# 7. 달력 틀 출력하기(다섯 주간)
calendar_string = """\
[{:04d}년 {:02d}월]________________
|Sun|Mon|Tue|Wed|Thu|Fri|Sat|
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
|---|---|---|---|---|---|---|
`````````````````````````````
"""
print(calendar_string.format(year, month))



this_month_string = """\
[2019년 09월]________________
|Sun|Mon|Tue|Wed|Thu|Fri|Sat|
| 01| 02| 03| 04| 05| 06| 07|
| 08| 09| 10| 11| 12| 13| 14|
| 15| 16| 17| 18| 19| 20| 21|
| 22| 23| 24| 25| 26| 27| 28|
| 29| 30| 31|---|---|---|---|
`````````````````````````````
"""