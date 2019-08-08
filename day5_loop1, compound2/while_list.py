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

