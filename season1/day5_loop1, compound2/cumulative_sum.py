# cumulative_sum.py
# 1) 1~100 의 총합 출력하기
# 2) 1~입력수 의 총합 출력

# 3) 입력수A~입력수B 의 총합 출력
print("두 수를 포함, 사이의 모든 정수 합을 출력합니다. ")
numA = input("첫번째 수: ")
numB = input("두번째 수: ")

sum_num = 0
i = numA
while i <= numB:
    sum_num += i
    i += 1

print("합은: " + str(sum_num))

# 4) 입력수A가 입력수B보다 크다면?

