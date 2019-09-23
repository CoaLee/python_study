# cond_elif.py

# elif 활용. 검사를 자세하게 해보자
age = input("나이를 입력해주세요")

if age >= 10 and age < 20:
    print("10대입니다.")
elif age >= 20 and age < 30:
    print("20대입니다.")
elif age >= 30 and age < 40:
    print("30대입니다.")
else:
    print("청춘입니다")     
print("검사 끝")

# 혹시 오류가 있을까?
# 좀더 간결하게 쓰는 방법은?