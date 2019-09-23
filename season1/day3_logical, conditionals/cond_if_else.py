# cond_if_else.py

if 5 < 10:
    print("5는 10보다 작습니다")

# 변수의 음수 여부를 판단해보자
numA = 7
if numA < 0: 
    print(str(numA) + "는 음수입니다.")

# 입력받은 수를 검사해보자
inNum = input("검사할 수를 입력해주세요: ")
if inNum % 3 == 0:
    print(str(inNum) + "는 __입니다.")  # 뭐라고 쓰면 될까요
else:
    print(str(inNum) + "는 __ 아닙니다.")

# 문자열 비교
word = "apple"
if (word == "apple"):
    print("참입니다")
    print("사과입니다")
    print("여러줄 쓸 수 있습니다")
    # 계산도 할수 있고 다 할수 있음
    numA = 123
    numB = 456
    print(numA + numB) 
else:
    print("사과 아닙니다")
print("여기는 무조건 실행되는 부분")