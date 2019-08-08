# times_table.py

print("구구단을 외자")

# 상태 변수 선언
a = 1
b = 1       # 에러
while a <= 9:                           # 진행 조건. a가 9까지는 나옴 
    print("---" + str(a) + "단---")     # 반복 내용
    while b < 10:                       # 이중 루프. 마찬가지 조건
        print(str(a) + " X " + str(b) + " = " + str(a * b))     # 좀 헷갈리지만..
        b += 1                          # 안쪽 루프 상태 변화
    a += 1                              # 바깥쪽 루프 상태 변화

print("구구단 끝")
