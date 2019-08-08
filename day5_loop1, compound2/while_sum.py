# while_sum.py
# 반복문으로 합 구하기

# 1) 1~10까지 더해보자
num = 1
sum_num = 0
while num < 11:
    sum_num += num
    num += 1
print(sum_num)

# 2) 1~10까지 짝수만 더해보자
num = 1
sum_num = 0
while num <= 10:
    if num % 2 == 0:
        sum_num += num
    num += 1
print(sum_num)

# 2-2) 다른 방법?
num = 2
sum_num = 0
while num <= 10:
    sum_num += num
    num += 2
print(sum_num)

# 2-3) 또 다른 방법??

