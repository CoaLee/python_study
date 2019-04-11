# exercise2_calc.py
# 계산기: 사칙연산 결과 나타내기

# 인트로 
print("--- 하랑 계산기 ver 1.0 ---")
print("두 정수를 입력하면 사칙연산 결과를 내보내겠소.")

# 입력 받기
strA = input("첫번째 수는 무엇이오: ")
strB = input("두번째 수를 알려주시오: ")
# 입력으로부터 정수로 변환하기. 매번 해도 되지만 이렇게 하는게 편할 것 같다.
numA = int(strA)
numB = int(strB)

# 출력하기. 문자열 덧셈 연산과 정수 사칙연산 
print(strA + " + " + strB + " = " + numA + numB)
print(strA + " - " + strB + " = " + numA - numB)
print(strA + " X " + strB + " = " + numA * numB)
print(strA + " / " + strB + " = " + numA / numB)

print("--- 계산 완료 ---")