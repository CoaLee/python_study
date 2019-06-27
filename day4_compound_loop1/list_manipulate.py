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