# op_comparison.py

print(1 > 5)
print("2 <= 7.5: " + str(2 <= 7.5))  # Wrong

# 변수 활용하기
A = 20
B = 40
print(str(A) + " >= " + str(B) + ": " + str(A >= B))


# 위와 같은 형식으로 변수 C와 D가 같은지 다른지를 확인하는 코드를 작성해보자
C = 4783294    # 변수 선언
D = 462348    # 변수 선언
print(str(A) + " == " + str(B) + ": " + str(A == B))    # 같은지 확인
print(str(A) + " != " + str(B) + ": " + str(A != B))    # 다른지 확인


# 문자열 비교
print("harang" < "programming")     # 
print("123" < "456")                # 
# print("123" < 456)      # TypeError

# 타입 확인
print(type(A) == str)           # False
print(type(A >= C) == int)      # bool == int  False





