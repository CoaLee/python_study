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
print()
print(list)
print(type(list))
print(dir(list))