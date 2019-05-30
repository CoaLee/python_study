# cond_elif.py

# elif 활용. 검사를 자세하게 해보자
age = input("나이를 입력해주세요: ")

if age >= 10 and age < 20:
    print("10대입니다.")
elif age >= 20 and age < 30:
    print("20대입니다.")
elif age >= 30 and age < 40:
    print("30대입니다.")
else:
    print("40대 이상입니다")     
print("검사 끝")

# 혹시 오류가 있을까?
# 좀더 간결하게 쓰는 방법은?  


inNum = input("수를 입력해주세요")
if inNum > 0:
    if inNum % 2 == 0:
        print("짝수입니다")
    else:
        print("홀수입니다")
else:
    print("음수입니다")
print(str(inNum) + "에 대한 검사 끝났습니다")
