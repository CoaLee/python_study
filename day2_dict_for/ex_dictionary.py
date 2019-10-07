# 딕셔너리 연습: 프터디 인명부 만들기
## 필요한 key들을 정하고 각 사람에게 맞춰서 만들어보기. favorite_season, birthday, age, hobby, etc ...
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

# 출력하는 방법을 만들어보자
print('이름:\t{}\n고향:\t{}\n전공:\t{}\n최애음식:\t{}'.format(yongjae['name'], yongjae['hometown'], yongjae['major'], yongjae['favorite_food']))
print('이름:\t{}\n고향:\t{}\n전공:\t{}\n최애음식:\t{}'.format(harim['name'], harim['hometown'], harim['major'], harim['favorite_food']))

## 반복작업이 번거롭다. 개선해보면?
member = study_members['이용재']
print('이름:\t{}\n고향:\t{}\n전공:\t{}\n최애음식:\t{}'.format(member['name'], member['hometown'], member['major'], member['favorite_food']))
member = study_members['여하림']
print('이름:\t{}\n고향:\t{}\n전공:\t{}\n최애음식:\t{}'.format(member['name'], member['hometown'], member['major'], member['favorite_food']))

# 여전히 번거롭다.. 이따 개선해보자