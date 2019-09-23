# Lecture4. Compound Data Types, Loop Statement
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

#### midterm 풀어보기

---
## 1. 복합 자료형1: 리스트 자료형
#### Why and What?
- Why? 자료가 묶음으로의 의미를 가진다(정보의 보존), 묶어두고 관리하면 편리하다
    - ex) 음악 앨범 속 곡들, 전화번호부, 투두리스트
    - 프로그래밍에서 '묶음'과 '의미 붙이기'의 중요성. &rarr; 함수, 클래스
- What?
    - 묶기, 꺼내쓰기, 수정하기
    - 리스트, 튜플, 딕셔너리
    - 오늘은 리스트부터

    |type|묶기|꺼내쓰기|수정하기|
    |---|---|---|:-:|
    |리스트| `[ val, ... ]` | `list[2]`| O |
    |튜플| `( val, ... )` | `tuple[4]`| X | 
    |딕셔너리| `{ 'key': value, ... }` | `dict['key']`| O |

#### How? List
1. 생성: 대괄호Bracket 안에 쉼표Comma로 구분
    - 빈리스트 생성 + 변수에 넣기: `listName = []`
    - 데이터와 함께: `myList = [1, 5.3, '문자열', "문자열", [1, 2]]`

2. 접근
    - Index: `myList[0]`, `myList[-2]`
    - Slicing: `myList[1:4]`, `myList[:2]` 

3. 조작: `dir(list)`로 확인. 이름으로 추측해보자
    - 추가하기: `append`, `insert`, `extend` | `+=`
    - 지우기: `remove`, `pop`, `clear` | `del myList[index]`
    - ...: `copy`, `count`, `index`, `reverse`, `sort`


### 코딩
```python
# list_creation.py

# 리스트를 쓰지 않는다면...
fruit1 = '귤'
fruit2 = '사과'
fruit3 = '바나나'
fruit4 = '자두'

# 리스트를 써보자
emptyList = []
fruits = ['귤', '사과', '바나나', '자두']
primesTen = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
movies = [
    '존윅3',
    '기생충',
    '알라딘',
    '토이스토리4',
]
mixed = [3.14, 2019, 'String', [1, 2, 3]]
listOfLists = [fruits, primesTen, movies, mixed]

print(emptyList)
print(fruits)
print(primesTen)
print(movies)
print(mixed)
print(listOfLists)

# 변수 이름으로 list는 사용 가능하지만 피하도록 하자
print(list)
print(type(list))
print(dir(list))
```
```python
# list_access.py

# 리스트 생성
studyMembers = ['JBK', 'LYR', 'YJW', 'CDJㅜ', 'JSY', 'YHR', 'LYJ']

# indexing
print(studyMembers)
print(studyMembers[0])
print(studyMembers[-1])
print(studyMembers[4] == studyMembers[-3])

# slicing
print(studyMembers[2:4])
print(studyMembers[:4])
print(studyMembers[4:])
print(studyMembers[1:-2])

# slicing with step
print(studyMembers[0:6:2])
print(studyMembers[0:6:-1])
```
```python
# list_manipulate.py

# 리스트 생성
studyMembers = ['JBK', 'LYR', 'YJW', 'CDJㅜ', 'JSY', 'YHR', 'LYJ']

# 값 수정하기: indexing으로 접근
studyMembers[3] = 'CDJ bye'
studyMembers[-1] = 'Yong'
studyMembers[9] = 'LKH'     # IndexError

# 값 추가하기: append, insert, extend
studyMembers.append('LKH')          # append: 뒤에 원소 붙이기
studyMembers.insert(2, 'PSH')       # insert: 특정 위치에 넣기
studyMembers.insert(-1, 'David')
studyMembers.insert(10000, 'Harang')
studyMembers.extend(['Keith', 'Peter', 'John'])     # extend 리스트 연장하기

# 값 지우기: remove, pop, clear, + del
studyMembers.remove('Yong')     # remove: 값 지우기
studyMembers.pop(3)             # pop: 특정 위치 값 뽑아내기
del studyMembers[2]             # del: 특정 위치 값 지우기
studyMembers.clear()            # clear: 다 지우기 

# 기타 연산:  +  *
numList = [1, 2, 3] + [-1, -2, -3]
print(numList)
numList = numList + [10, 20, 30]
print(numList)

greetMsgs = ['Hello', '안녕']
print(greetMsgs * 5)
```

## 2. `is`, `in` 관계 연산자
#### `is`
- 값이 같은지 비교하는 관계 연산자
- `==`과의 차이: 값 비교 vs. 주소 비교
- 변수: 값이 들어있는 봉투(세모) &rarr; 봉투의 주소를 저장(O)
- `id(val)`: 주소값 확인

#### `in`
- 특정 자료값이 복합자료형(리스트, 튜플, 딕셔너리)에 속해 있는지 확인하는 관계 연산자

### 코딩
```python
# is_comparison.py

a = [1,2,3]
b = a
c = [1,2,3]

print(id(a))
print(id(b))
print(id(c))

print(a == b)   # True
print(a == c)   # True 

print(a is b)   # True
print(a is c)   # False

d = [1,2,3]
e = [1,2]

print(id(d))
print(id(e))

print(d == e)   # False
print(d is e)   # False
del d[2]
print(d == e)   # True
print(d is e)   # False
```
```python
# in_comparison.py

primeNumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

print(7 in primeNumbers)
print(12 in primeNumbers)

inputNum = int(input("30 이하의 자연수를 입력해주세요: "))
isPrime = False

if inputNum > 30 or inputNum < 1:
    print("잘못된 입력입니다")
else:
    if inputNum in primeNumbers:
        isPrime = True

    if isPrime is True:
        print(inputNum + ": 소수입니다")
    else: 
        print(inputNum + ": 소수가 아닙니다")
```
---
## Exercise
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