# variable.py: 변수 선언과 활용

# 숫자 변수
num = 910618
print(num)

# 숫자 변수 연산
numA = 54
numB = 21
print(numA + numB)
print(numA * numB + numA / numB)

# 문자 변수
greeting = "안녕하세요"
print(greeting)
print("greeting")   # 차이를 알겠나요?

# 변수명은 한글도 된다. 변수명에 띄어쓰기는 하면 안됨)
한글도된다 = "Hello guys, how are you?"
print(한글도된다)

# 변수 값들을 연산해서 새로운 변수에 넣기. 저 위에서 선언한 변수 활용
numC = numA - numB
print(numC)

# 물론 자기 자신도 사용할 수 있음
numC = numC * numC
print(numC)