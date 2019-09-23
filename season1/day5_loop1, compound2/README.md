# Lecture5. While Loop
## 0. 복습
0. 프로그래밍 개념
    - 프로그래밍은 컴퓨터가 하는 일을 시키는 것이다
    - 컴퓨터는 데이터를 저장하고 연산하는 일을 잘한다
    - 프로그래밍과 코딩. 순서도. 레시피.

1. 표준 입출력
    - `print()` 함수
    - `input()` 함수
    - `input()`과 `input("어떤 말")`의 차이
    - 표준 입출력에서 '표준'의 의미: 키보드와 모니터

1. 변수
    - 데이터를 저장하고 계속 활용하기 위해서 봉투에 담는 것
    - 변수 선언: `=` 왼쪽에 변수 이름, 오른쪽에 값
    - 변수 사용: `=` 왼쪽이 아닌 곳에서 변수 이름

1. 기본 자료형: 정수, 실수, 문자열
    - 다루려는 자료를 확인하고 알맞게 다루기 위해
    - 요리 재료의 구분(채소, 고기, 향신로)과 비슷
    - 파이썬에서 자료형 결정은 자동(dynamic type check, 동적)으로 됨 
    - 자료형 확인은 `type()` 함수 활용 

1. 기본 연산자: 수 연산, 문자열 연산
    - 연산: 주어진 자료를 조작, 계산을 통해 원하는 값 얻기
    - 자료 &rarr; 연산 &rarr; 결과 &rarr; 저장 / 활용
    - 연산 중 기본이 되는 연산자
    - 수: `+`, `-`, `/`, `*`, `//`, `%`, `**`
    - 문자열: `+`, `*`

1. 논리 자료형
    - 논리값을 다루기 위해
    - `True`, `False`

1. 비교(관계) 연산자, 논리 연산자
    - 관계 연산자: 값 사이의 비교 &rarr; 논리값이 나옴
    - `>` , `>=` , `<` , `<=` , `==` , `!=`
    - 논리 연산자: 논리값들 사이의 연산
    - `A and B`, `A or B`, `not A`, `A && B`, `A || B`, `!A`

    | `A` | `B` | `A and B` | `A or B` | `not A` | `not (A and B)` |
    |:-:|:-:|:-:|:-:|:-:|:-:|
    |`False`|`False`|`False`|`False`|`True` |`True` |
    |`False`|`True` |`False`|`True` |`True` |`True` |
    |`True` |`False`|`False`|`True` |`False`|`True` |
    |`True` |`True` |`True` |`True` |`False`|`False`|

1. 조건문
    - 프로그램 실행 중 경로가 달라져야 할 때
    - 특정 조건을 검사하고, 해당 코드들을 배치
    ```python
    if cond1:
        statements...
    elif cond2:
        statements...
    else:
        statements...
    ```
    - `cond`: 논리값이 나오는 식(ex. `var > 0`, `var >= 20 and var < 30`)

1. 복합자료형
    - 묶음으로 의미를 가질 때
    - 자료들을 묶어두고, 활용하기
    - 종류: 리스트(list), 튜플(tuple), 딕셔너리(dictionary)

    |type|묶기|꺼내쓰기|수정하기|
    |---|---|---|:-:|
    |리스트| `[ val, ... ]` | `list[2]`| O |
    |튜플| `( val, ... )` | `tuple[4]`| X | 
    |딕셔너리| `{ 'key': value, ... }` | `dict['key']`| O |

1. 리스트
    - 생성: 대괄호Bracket 안에 쉼표Comma로 구분
        - 빈리스트 생성 + 변수에 넣기: `listName = []`
        - 데이터와 함께: `myList = [1, 5.3, '문자열', "문자열", [1, 2]]`
    - 접근
        - Index: `myList[0]`, `myList[-2]`
        - Slicing: `myList[1:4]`, `myList[:2]` 
    - 조작: `dir(list)`로 확인. 이름으로 추측해보자
        - 추가하기: `append`, `insert`, `extend` | `+=`
        - 지우기: `remove`, `pop`, `clear` | `del myList[index]`
        - ...: `copy`, `count`, `index`, `reverse`, `sort`

1. 기타 관계 연산자
    - `is`
        - 같은 자료인지 확인. 주소값 비교
        - `==`과의 차이: 값 비교 vs. 주소 비교
        - `id(val)`: 주소값 확인
    - `in`
        - 특정 자료값이 복합자료형(리스트, 튜플, 딕셔너리)에 속해 있는지 확인하는 관계 연산자
---
## Remind Exercise
```python
# list_repetition.py

foods = []
print("좋아하는 음식 5개를 입력해 주세요.")

tmpFood = input("1번째 음식: ")
foods.append(tmpFood)

tmpFood = input("2번째 음식: ")
foods.append(tmpFood)

tmpFood = input("3번째 음식: ")
foods.append(tmpFood)

tmpFood = input("4번째 음식: ")
foods.append(tmpFood)

mpFood = input("5번째 음식: ")
foods.append(tmpFood)

print("좋아하는 음식들:")
print(foods[0])
print(foods[1])
print(foods[2])
print(foods[3])
print(foods[4])

print("좋아하는 음식 top 3:", foods[:3])

toRemove = input("지우고 싶은 음식: ")
foods.remove(toRemove)
```
---
## 1. 반복문1: while 
#### Why and What?
- Why? 
    - 반복되는 작업(단순 반복, 복합자료형 접근)
    - '반복해서 쓰기 귀찮다', '줄이고 싶다.. 줄이고 싶다...'
    - 간단한 표현 &rarr; 이해, 관리, 수정에 용이
    ![computational thinking](../computational_thinking.png)
- What?
    - 초기 상태 설정, 진행 조건 걸기
    - 반복되는 부분 묶어서 표현하기
    - 바뀌는 부분은 바뀌도록 하기


#### How? `while`, `for` 중 `while` 먼저
```python
초기 상태(상태 변수) 설정
while 진행 조건:
    반복시킬 문장들. 블럭 안
    상태 변수 변경
    ...
반복 안될 문장들. 블럭 밖
```
```python
i = 0
while i < 10:
    print(i)
    i = i + 1
```
1. 초기 상태, 진행 조건
    - 상태 변수 설정
    - 진행 조건: `True`일 동안 반복문 실행

2. 반복 부분 표현
    - `while 조건:` 다음에 **띄어쓰기 4회**(<kbd>TAB</kbd>)로 블럭 표현

3. 바뀌는 부분 바뀌도록
    - 반복문 안에서 상태 변수 변화시키기
    - 상태 변수 활용

### 코딩
#### while 기본
```python
# while_basic.py
# while 반복문 기본

print("반복문 시작")    # 반복문 이전 작업

i = 0                  # 초기 상태 설정. 상태 변수 선언
while i < 5:           # while과 진행조건 적기. : 찍고 블럭으로
    print(i * 5)       # 반복할 내용
    i = i + 1          # 상태 변수 변화(이것 역시 반복하는 것). 이 변화가 없다면? 실험해보자

print("반복문 끝")      # 반복문 다음 작업
```
#### 위에서 만들었던거 줄여보기
```python
# list_repetition_while.py
# 반복 작업 줄여보기
# 작성했던거 복사 + 붙여넣기 후 수정합시다

foods = []

# 첫번째 반복문. 반복 입력
print("좋아하는 음식 5개를 입력해 주세요.")
i = 1
while i <= 5:
    tmpFood = input(str(i) + '번째 음식: ')
    foods.append(tmpFood)
    i += 1

# 두번째 반복문. 반복 출력 
print("좋아하는 음식들:")
i = 0
while i < 5:
    print(foods[i])

print("좋아하는 음식 top 3:", foods[:3])

toRemove = input("지우고 싶은 음식: ")
foods.remove(toRemove)
```
#### 반복문으로 합 구하기
```python
# while_sum.py
# 반복문으로 합 구하기

# 1) 1~10까지 더해보자
num = 1
sum_num = 0
while num < 11:
    sum_num += num
    num += 1
print(sum_num)

# 2) 1~10까지 짝수만 더해보자
num = 1
sum_num = 0
while num <= 10:
    if num % 2 == 0:
        sum_num += num
    num += 1
print(sum_num)

# 2-2) 다른 방법?
num = 2
sum_num = 0
while num <= 10:
    sum_num += num
    num += 2
print(sum_num)

# 2-3) 또 다른 방법??

```
#### 다중 반복문
```python
# while_nested.py
# 반복문 안에 반복문도 가능하다

```
#### 반복문 + 리스트
```python
# while_list.py

# 복붙합시다 from 'day4/list_access.py'
studyMembers = ['JBK', 'LYR', 'YJW', 'CDJㅜ', 'JSY', 'YHR', 'LYJ']

# 1) 반복 출력 + 첫번째 문자열 interpolation (보간?)
i = 0
while i < 7:
    print(f'{i}번째 스터디 멤버: {studyMembers[i]}. 파이팅!')
    i += 1

# 2) 사람 찾기 + 두번째 string interpolation 
search = input("찾으려는 사람 이니셜: ")
i = 0
while i < len(studyMembers):
    if studyMembers[i] == search:
        print('{}는 {}번째 스터디 멤버. 파이팅!'.format(search, i + 1))
    i += 1

# 3) 찾지 못했을 경우에 찾지 못했다고 출력하고 싶은데?

```
---
## Exercise
```python
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

```
```python
# times_table.py

print("구구단을 외자")

# 상태 변수 선언
a = 1
b = 1       # 에러
while a <= 9:                           # 진행 조건. a가 9까지는 나옴 
    print("---" + str(a) + "단---")     # 반복 내용
    while b < 10:                       # 이중 루프. 마찬가지 조건
        print(str(a) + " X " + str(b) + " = " + str(a * b))     # 좀 헷갈리지만..
        b += 1                          # 안쪽 루프 상태 변화
    a += 1                              # 바깥쪽 루프 상태 변화

print("구구단 끝")
```
```python
# times_table_enhanced.py

print("구구단을 외자")
end = input("몇단까지?: ")

a = 1                                   # 상태 변수 선언
while a <= end:                         # 진행 조건. a가 9까지는 나옴 
    print("---" + str(a) + "단---")     # 바깥 루프 반복 내용
    b = 1                               # 상태 변수 선언
    while b < end + 1:   # 약간 에러     # 이중 루프. 마찬가지 조건
        print(str(a) + " X " + str(b) + " = " + str(a * b))     # 좀 헷갈리지만..
        b += 1                          # 안쪽 루프 상태 변화
    a += 1                              # 바깥쪽 루프 상태 변화

print("구구단 끝")
```