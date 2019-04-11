# exercise2_hello.py
# 인사 상호작용: 사용자 정보 입력 받고 맞춰서 출력하기

# 인트로 
print("--- 인사 맞이 프로그램 ---")
print("안녕하세요 :)")
print("당신에 대해서 알려주세요")

# 기본 정보 입력 
name = input("이름: ")
hometown = input("고향: ")

age = int(input("몇 살인가요? "))
birth_year = int(input("태어난 연도를 알려주세요: "))
birth_month = int(input("태어난 월과: "))
birth_date = int(input("태어난 날짜도요: "))

# 기본 정보 가지고 출력하기 
print(hometown + "에서 태어난 " + name + "님 반갑습니다!")
print("기본적인 정보를 입력 받았습니다. 추가 정보를 입력해주세요.")

# 부가 정보 입력
major = input("전공: ")
bucket_list1 = input("버킷 리스트 첫번째: ")
bucket_list2 = input("버킷 리스트 두번째: ")
favorite_food = input("좋아하는 음식은? ")

# 부가 정보 가지고 출력하기
print(major + "전공을 가진 " + name + "님의 버킷리스트: ")
print("1. " + bucket_list1)
print("2. " + bucket_list2)

# 인사
print("버킷 리스트 꼭 달성하길! 안녕히 가세요 :)")