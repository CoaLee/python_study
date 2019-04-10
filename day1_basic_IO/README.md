# Lecture 1. Programming Basic, Standard IO, Variable
## 0. 프로그래밍 개념
### 개념정리
- 프로그래밍? 프로그램을 만드는 것
- 프로그램? 특정한 목적을 가진 일련의 순서, 과정
- 컴퓨터프로그램? 컴퓨터가 수행하는, 특정한 목적을 가진 일련의 작업 순서, 과정
- 특정한 목적?? 
- 컴퓨터? 계산기
- 컴퓨터가 **잘**하는 작업? 정보(데이터)의 저장(표현) 및 연산(처리)
* 컴퓨터 프로그래밍:
    1. 왜? 특정 목적을 달성하기 위해,
    2. 무엇? 컴퓨터에게 일(일련의 작업)을 시키는 것
    3. 어떻게? 정보의 저장 및 연산 **작업을 구상**
    4. 어떻게? 구상한 작업을 컴퓨터한테 알려주기 &rarr; *코딩*
- 프로그래밍 언어? 컴퓨터한테 해야할 작업(프로그램)을 알려주기 위한 언어
- 어떻게 알아듣나? 번역 번역 번역

### 이해를 돕기 위한 비유들
1. 내가 말하는 내용이 언어를 통해 상대방의 귀에 들리고, 그 언어를 해석하여 내용을 파악함
2. 건축에 있어서 설계가 중요하다 &rarr; 프로그래밍에 있어서 구상 단계가 중요하다
3. 건축 디자인을 하고 나서 시공 단계. 재료의 특성 &rarr; 프로그래밍 언어의 차이
4. 같은 한글을 쓰지만, 모두 다른 일을 한다 &rarr; 프로그래밍 언어로 할 수 있는 일, 만들 수 있는 프로그램의 다양성
5. 같은 한글을 쓰지만, 작가가 될수도 있고 쓸데 없는 말을 할 수도 있다 &rarr; 내용의 중요성
6. 같은 카카오톡. Android, iOS, 데스크탑 버전이 있는 것

---
## 1. Python Programming
### Why Python?
1. 배우기 쉽다, 읽기 쉽다
2. 핵심적인 프로그래밍 아이디어는 서로 비슷하다
3. 다양한 라이브러리 &rarr; 활용가능성이 많다 (웹 프로그래밍, 빅데이터, 머신러닝)

### 개발환경
- Python ([Download](https://www.python.org/downloads/)) - Language Interpreter
- VS Code ([Download](https://code.visualstudio.com/)) - Code Editor

### 순서대로 세팅
1. Python 다운로드, 설치하기
2. `PATH` 변수 설정: 경로를 적어둠으로써 이름만으로 찾아서 실행할 수 있도록 함
3. cmd로 실행해보기
    1. cmd 실행: <kbd>win</kbd> + <kbd>R</kbd> - `cmd` 입력
    2. 설치 확인: `python --version`
    3. **인터프리터 실행**
        1. `python3`
        2. 입력해보기: `1 + 2` , `2 * 5 / 10` , `Hi` , `"Hi"` , `"hello, world"` , `'this is string'`
    4. 위치 이동: `cd \` - `dir` - `mkdir workspace` - `cd workspace`
    5. **소스파일 실행**
        1. `echo print("hello world") > test.py`: 파일 만들기
        2. `cat test.py`: 파일 내용 확인
        3. `python3 test.py`: 인터프리터한테 읽고 실행시키도록
4. vscode 다운로드, 설치하기
    1. 필요한 추가기능 설치: <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>X</kbd> or `[View]` - `[Extensions]`
        - python 설치
        - (선택) korean language pack 설치
    2. (선택) <kbd>F1</kbd> or <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> &rarr; color theme 검색
    3. `[File]` - `[Open Folder]` &rarr; `workspace` 폴더 찾아서 열기, `day1` 폴더 만들기
    4. <kbd>Ctrl</kbd>+<kbd>N</kbd> &rarr; <kbd>Ctrl</kbd>+<kbd>S</kbd> &rarr; `hello.py` 저장
    5. `print("Hello Yongjae")` 입력하고 저장
    6. cmd로 실행
    7. <kbd>Ctrl</kbd>+<kbd>`</kbd>(backtick: 숫자 1 왼쪽)로 실행
    8. `# 주석(Comment)`: 컴퓨터가 아닌 사람을 위한 문장. 주로 코드에 대한 설명 및 부가 정보를 적음. 인터프리터는 해석하지 않는다.

---
## 2. 표준 입출력 
#### Why and What?
- Why? 프로그램 = 데이터 처리 작업. 처리하려면 데이터가 있어야 하고, 처리 결과를 확인하고 싶다.
- What? 데이터 입력 &rarr; 작업 &rarr; 결과 출력

#### How?
1. 출력: `print(출력할 데이터)` &rarr; `출력할 데이터`를 출력해라
2. 입력: `input()` &rarr; 사용자 입력을 기다리다가 엔터 치면 받아라
3. 힌트랑 입력: `input("힌트 문자열")` &rarr; `힌트 문자열`을 출력하고서, 사용자의 입력을 받아라

### 코딩
```python
# print.py : print로 출력 연습

print("Hello World")
print('안녕 세상')
print(안녕하세요) # ValueError
print(3 + 5)    # 8
print("3 + 5")  # '3 + 5'
```
```python
# input.py : input으로 입력 연습

input("아무거나 입력해주세요")
print("아무거나 입력해주시죠")
input()
```
```python
# input_print.py : 입력 받아서 출력하기

print("이름: ")
print(input())
print("님 안녕하세요")

print(input("나이: "))
print("한창 젊은 나이입니다!!")
```
---
## 3. 변수 (1강 때 못하고 2강에서 다룰 예정)
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