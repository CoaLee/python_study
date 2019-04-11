# Lecture2. Variable, Primitive Data Types, Operators
> 생각: 관통프로젝트처럼 한가지 프로그램을 정하고서 살을 붙여나가볼까? 전체 다는 못하더라도. 오늘 할것들만 합쳐서라도.

## 0. 복습 (실행결과 예측 퀴즈)
- 프로그래밍은 컴퓨터가 하는 일을 시키는 것이다
- 컴퓨터는 데이터를 저장하고 연산하는 일을 잘한다
- 왜 해야하는지 생각해보기 
- `print()`
- `input()`
- `input()`과 `input("어떤 말")`의 차이


## 1. 변수
#### Why and What?
- Why? 데이터 처리할건데, 데이터를 계속해서 사용할 필요가 있다 &rarr; 데이터를 저장해두고 싶다
- What? 변수: 데이터에 이름을 붙인 것. 데이터를 담아두는 봉투 / 그릇

#### How?
1. 변수 선언: `variable_name = value` &rarr; 봉투에 값 넣어두고 이름 붙이기
2. 변수 사용: `' = '` 의 왼쪽이 아닌 곳에서 `variable_name` &rarr; 봉투 이름으로 봉투 찾아서 들어있는 값 확인
3. 변수명 정하기
    - 알파벳, 한글, 숫자, _
    - 대소문자 구분, `keywords` 안됨
    - 의미 있는 이름 붙이기. **중요함**. `cnt = 123`과 `t = 123'`의 차이
        - > 인용: 코드는 사람이 읽기 위해 쓰여진 것, 컴퓨터가 우연히 읽을수 있다면 좋은것
        - 프로그래머가 힘들어하는 일
        ![프로그래머가 힘들어하는 일](programmer_job.png "프로그래머가 힘들어하는 일")

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

# 변수명은 한글도 된다. 변수명에 띄어쓰기는 하면 안됨)
한글도된다 = "Hello guys, how are you?"
print(한글도된다)

# 변수 값들을 연산해서 새로운 변수에 넣기. 저 위에서 선언한 변수 활용
numC = numA - numB
print(numC)

# 자기 자신도 마찬가지
numC = numC * numC
print(numC)


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
print("살이군요. 건강하세요. 파이팅!")
```

---
## 2. 자료형
#### Why and What?
- Why? 다루려는 자료가 어떤 종류인지 파악하기 위해, 알맞게 다루기 위해
    ex) 핸드폰과 망치 / 음식과 옷
- What? (실습)
    1. 수 자료형: `7`, `3.14`, `-243`, `0x1fa0`, `0o247`, `0b101101`, `1 + 4j`
    2. 문자열 자료형: `'작은 따옴표 문자열'`, `"큰 따옴표 문자열"`, `''`, `'''여러줄'''`, `"""여러줄"""`, `'\n\t'`
    3. 논리 자료형: `True`, `False`

#### How?
1. 자료형 결정: 자동(dynamic type check)으로. `str = "문자열"`
    - 비교: C에서는 `char[] str = "문자열";` Java에서는 `String str = "문자열";`
2. 자료형 확인: `type( variable )`, `type( "data" )`, `type( 145.73 )`, ...

### 코딩
```python
# type_num.py

20190411
3.1415926535897
-273

date_int = 20190411
pi_float = 3.14
absolute_zero_celcius = -273
remaining_days = -273
```
```python
# type_str.py

'이것은 문자열'
"이것도 문자열"

name = 'Yongjae'

single_quote = 'Single quotation mark. "double quote" can be used'
print(single_quote)

double_quote = "쌍따옴표 문자열. 문자열 안에 '작은 따옴표'"
print(double_quote)

multi_line_str = '''this is multi line str
second line
third line
'''
print(multi_line_str)
```
```python
# type_boolean.py

True
False

true_var = True
is_earth_bigger_than_sun = False
am_I_graduated = True
```
```python
# type_var_exercise.py

# 자신과 관련된 정보를 적어보자
name = 'Yongjae'
nickname = "머큰용"

age = 29
birth_year = 1991
birth_month = 6
birth_date = 18

major = '컴퓨터공학'
hometown = '가평군 조종면'
phone_number = '01095031381'
bucket_list1 = '수만명이 사용하는 서비스 개발'
bucket_list2 = '돈 "많이" 벌어서 잘 사용하기'
favorite_food = '김치 닭도리탕'
# 기타 좋아하는 무언가 두개 적어보기 좋아하는 영화, 색, 계절, 숫자, 가수 등등
```

---
## 3. 연산
#### Why and What?
- Why? 
- What? 

#### How?
1. 수 연산: `+`, `-`, `*`, `/`, `%`, `//`

2. 문자열 연산: `+`, `*`

3. 관계 연산: `>`, `>=`, `<`, `<=`, `==`, `!=`, `is`

4. 논리 연산: `and`, `or`, `not`, `&&`, `||`, `!`

*  자료형 변환: `int('123')`, `str(545)`


### 코딩
```python
# op_arithmetic.py

```
```python
# op_string.py

```
```python
# op_relation_and_logic.py

```
```python
# op_cast.py

```