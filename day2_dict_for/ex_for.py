# for 연습
## 구구단 출력하기
for a in range(1, 10):
    for b in range(1, 10):
        print(f'{a} X {b} = {a * b}')

## 일구일구단 출력하기
for a in range(1, 20):
    for b in range(1, 20):
        print(f'{a} X {b} = {a * b}')

## NN단 출력하기
N = int(input("몇단까지? "))
for a in range(1, N):
    for b in range(1, N):
        print(f'{a} X {b} = {a * b}')


## 아까 딕셔너리 연습에서 만들었던 부분을 for 문을 활용해 바꿔보자
yongjae = {'name': '이용재', 'hometown': '신하리', 'major': '자유전공학부', 'favorite_food': '김치 닭도리탕'}
harim = {
    'name': '',
    'hometown': '',
    'major': '',
    'favorite_food': ''
}
study_members = {
    '이용재': yongjae, 
    '여하림': harim
}

## 반복작업이 번거롭다. 개선해보면?
member = study_members['이용재']
print('이름:\t{}\n고향:\t{}\n전공:\t{}\n최애음식:\t{}'.format(member['name'], member['hometown'], member['major'], member['favorite_food']))
member = study_members['여하림']
print('이름:\t{}\n고향:\t{}\n전공:\t{}\n최애음식:\t{}'.format(member['name'], member['hometown'], member['major'], member['favorite_food']))

## 바꿔보면
for member in study_members.values():
    for key, value in member.items():
        print(f'{key}:\t{value}')