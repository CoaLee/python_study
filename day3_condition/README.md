# Lecture3. Logical Data Types, Logical Operators, Conditional Statement
## 0. 복습
0. 프로그래밍 개념
    - 프로그래밍은 컴퓨터가 하는 일을 시키는 것이다
    - 컴퓨터는 데이터를 저장하고 연산하는 일을 잘한다
    - 왜 해야하는지 생각해보기 

1. 파이썬 프로그래밍
    - 개발환경 세팅: Python(interpreter), VS code(text editor) 설치
    - 인터프리터 실행
    - 소스코드 실행 (<kbd>Ctrl</kbd>+<kbd>N</kbd> &rarr; <kbd>Ctrl</kbd>+<kbd>S</kbd> &rarr; 콘솔 실행(<kbd>Ctrl</kbd>+<kbd>\`</kbd> / `cmd`)

2. 표준 입출력
    - `print()`
    - `input()`
    - `input()`과 `input("어떤 말")`의 차이
    - 표준 입출력에서 '표준'의 의미: 키보드와 모니터

3. 변수

4. 기본 자료형: 정수, 실수, 문자열

5. 기본 연산자: 수 연산, 문자열 연산
    1. 수 연산자: `+`, `-`, `*`, `/`, `%`, `//`, `**`
    2. 문자열 연산자: `+`, `*`


## 1. 논리 자료형 & 연산자 
#### Why and What?
- Why? 논리적인 의미를 표현하기 위해
- What? 참(`True`) / 거짓(`False`)

#### How?
1. 참: `True`
2. 거짓: `False`

```python
# type_boolean.py

True    # not true
False   # not false

yongIsSmart = True


```

## 2. 논리 연산자
#### Why and What?
- Why?
- What?

#### How?
1. 비교 연산자
    - `>` , `>=` , `<` , `<=` , `==` , `!=`
2. 논리 연산자
    - `A and B`: 양쪽 다 True면 True  ( `A && B` )
    - `A or B`: 한 쪽이라도 True면 True ( `A || B` )
    - `not A`: A가 True 면 False, A가 False면 True ( `!A` )

    | `A` | `B` | `A and B` | `A or B` | `not A` | `not (A and B)` |
    |:-:|:-:|:-:|:-:|:-:|:-:|
    |`False`|`False`|`False`|`False`|`True` |`True` |
    |`False`|`True` |`False`|`True` |`True` |`True` |
    |`True` |`False`|`False`|`True` |`False`|`True` |
    |`True` |`True` |`True` |`True` |`False`|`False`|

### 코딩
```python
# op_comparison.py


```

```python
# op_logic.py

```

```python

```

## 3. 조건문 
#### Why and What?
- Why? 프로그램의 실행 중, 조건에 따라 다르게 실행하고 싶다
- What? 

#### How?
1. `if [condition]:` 
2. 한 탭(스페이스 네번) **들여쓰기** 이후 내용 적기
3. `else:`

#### ※ Block 개념
- 프로그래밍 언어에서 코드들의 묶음
- python 에서는 탭(스페이스 4)으로 구분

### 코딩
```python
# cond_if_else.py


```
```python
# cond_elif.py


```

