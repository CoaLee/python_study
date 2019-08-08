# times_table_enhanced.py

print("구구단을 외자")
end = input("몇단까지?: ")

a = 1                                   # 상태 변수 선언
while a <= end:                         # 진행 조건. a가 9까지는 나옴 
    print("---" + str(a) + "단---")     # 바깥 루프 반복 내용
    b = 1                               # 상태 변수 선언
    while b < end + 1:   # 약간 에러     # 이중 루프. 마찬가지 조건
        print(str(a) + " X " + str(b) + " = " + str(a * b))     # 좀 헷갈리지만..
        b += 1                          # 안쪽 루프 상태 변화
    a += 1                              # 바깥쪽 루프 상태 변화

print("구구단 끝")
