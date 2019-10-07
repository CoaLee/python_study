'''
# 딕셔너리

딕셔너리: 복합자료형 3남매 중 둘째. 기억력이 좋고 유연하며, 개성이 있다. 
- 3남매의 인생 고민: 묶어둔 데이터를 어떻게 구분할 것인가? == 자료를 어떻게 넣어두고 어떻게 꺼내어 쓸 것인가?
- 리스트, 튜플: 순서대로, 정수 인덱스를 사용해서
- 딕셔너리: 순서가 아닌, 자료(value)에 특정한 의미(key)를 붙여서. key-value pairs
- mutable. 추가, 수정, 삭제 가능

생성하기
- {} 로 생성
{ key1: value1, key2: value2, ... }
{ 
    key1: value1,
    key2: value2,
    ...
}
- key: 기본 자료형(문자열, 숫자) 올 수 있음
- value: 아무거나 다 됨

접근, 수정, 삭제는 실습을 통해서

'''

# 1. 딕셔너리 생성, 값 접근
my_phone = { 'brand': 'Samsung', 'model': 'Note9' }
print(type(my_phone))
print(my_phone)
print(my_phone['brand'])


# 2. 추가, 수정, 삭제
my_phone['OS'] = 'Android'
my_phone['price'] = 200000
print('price: {}'.format(my_phone['price']))
my_phone['price'] = 250000
print(f'price: {my_phone["price"]}')
my_phone['price'] *= 1.10
print(my_phone)

del my_phone['OS']
print(my_phone)
my_phone.pop('price')

## 근데 실제로는 삭제를 많이 쓰지는 않는 것 같다.
## 나중에 배우게 될 클래스의 개념과 비슷한 면이 있다.