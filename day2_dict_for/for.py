'''
# for loop (반복문2)

옛날 옛적에, while이 있었다
- 주로 활용되는 모습을 보아하니,
    1. 수(상태 변수)를 증가시키면서 활용
    2. 복합 자료형 자료들에 접근
- "특정한 패턴에는 보다 간결한 문법을 만들어 보자!" 해서 나온 것이 for


for 문법
>   for [변수] in [반복가능객체묶음]:
>       [변수] 활용한 작업들
>       ...

Q. [반복가능객체묶음]?: 영어로 iterable. 우선은 간단하게 순서가 있는 복합 자료형(리스트)이라고 생각
Q. while문은 어떻게 쓰더라? while문과의 차이점은?


나머지는 실습을 통해서

'''

# 0. while문부터 기억해보자
studyMembers = ['JBK', 'LYR', 'YJW', 'CDJㅜ', 'JSY', 'YHR', 'LYJ']

## 1) 반복해서 리스트 출력 + 첫번째 문자열 interpolation (보간?)
## 2) 사람 찾기 + 두번째 string interpolation 



# 1. for 문 활용하기: 리스트 자료 접근하기. 위 while문을 바꿔보면

## enumerate 활용



# 2. for 문 활용하기: 일정하게 변하는 수
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]   # ???
for i in numbers:
    print(i)

# range(b):         0 <= n < b, 간격 1
# range(a, b):      a <= n < b, 간격 1
# range(a, b, c):   a <= n < b, 간격 c

# range(a, b, c):   a >= n > b, 간격 c    if (c < 0)



# 3. for 문 활용하기: 딕셔너리 자료 접근하기
## dict.keys(), dict.values(), dict.items()
capitals = {'한국': '서울', '캐나다':'오타와', '호주':'캔버라'}

