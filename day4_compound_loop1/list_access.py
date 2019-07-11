# list_access.py

# 리스트 생성
studyMembers = ['JBK', 'LYR', 'YJW', 'CDJㅜ', 'JSY', 'YHR', 'LYJ']

# indexing
print(studyMembers)
print(studyMembers[0])
print(studyMembers[-1])
print(studyMembers[4] == studyMembers[-3])

# slicing
print()
print(studyMembers[2:4])
print(studyMembers[:4])
print(studyMembers[4:])
print(studyMembers[1:-2])

# slicing with step
print()
print(studyMembers[0:6:2])
print(studyMembers[::-1])