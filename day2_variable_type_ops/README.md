# Lecture2. Variable, Primitive Data Types, Operators
## 0. 복습 (퀴즈로?)
- print()
- input()
- input()과 input("어떤 말")의 차이


## 1. 변수
#### Why and What?
- Why? 데이터 처리할건데, 데이터를 계속해서 사용할 필요가 있다 &rarr; 데이터를 저장해두고 싶다
- What? 변수: 데이터에 이름을 붙인 것. 데이터를 담아두는 봉투 / 그릇

#### How?
1. 변수 선언: `variable_name = value` &rarr; 봉투에 값 넣어두고 이름 붙이기
2. 변수 사용: `variable_name` &rarr; 봉투 이름으로 봉투 찾아서 들어있는 값 확인하기

### 코딩
```python
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

# 변수명은 한글도 된다. 변수명에 띄어쓰기는 하면 안됨
한글도된다 = "Hello guys, how are you?"
print(한글도된다)
```
```python
# hello_variable.py : 변수와 input, print 합쳐서 활용

# 인사는 내가 먼저
print("=== 인사 프로그램 ver 1.0 ===")
print("안녕하세요. 당신을 소개해주세요")

# 입력 받기
name = input("이름이 뭐예요: ")
age = input("나이는요?: ")

# 데이터 저장한 변수를 활용해서 출력하기
print(name)
print("님 안녕하세요. 반갑습니다.")
print(name)
print("님은")
print(age)
print("살이군요. 청춘 파이팅!")
```

---
## 2. 자료형
#### Why and What?
- Why? 다루려는 자료가 어떤 종류인지 파악하기 위해, 알맞게 다루기 위해
    ex) 핸드폰과 망치 / 음식과 옷 / '참' + 123 ?
- What?
    1. 수 자료형: `7`, `3.14`, `-243`, `0x1fa0`, `0o247`, `0b101101`, `1 + 4j`
    2. 문자열 자료형: `'작은 따옴표 문자열'`, `"큰 따옴표 문자열"`, `''`, `'''여러줄'''`, `"""여러줄"""`, `'\n\t'`
    3. 논리 자료형: `True`, `False`

#### How?
1. 자료형 정의: 자동으로. dynamic type check
2. 자료형 확인: `type( variable )`, `type( "data" )`, `type( 145.73 )`, ...

### 코딩

---
## 3. 연산
#### Why and What?
- Why?
- What?

#### How?
1. 수 연산

2. 문자열 연산

3. 논리 연산


### 코딩
```python

```