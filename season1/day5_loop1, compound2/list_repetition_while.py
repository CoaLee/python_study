# list_repetition_while.py
# 반복 작업 줄여보기
# 작성했던거 복사 + 붙여넣기 후 수정합시다

foods = []

# 첫번째 반복문. 반복 입력
print("좋아하는 음식 5개를 입력해 주세요.")
i = 1
while i <= 5:
    tmpFood = input(str(i) + '번째 음식: ')
    foods.append(tmpFood)
    i += 1

# 두번째 반복문. 반복 출력 
print("좋아하는 음식들:")
i = 0
while i < 5:
    print(foods[i])
    i += 1

print("좋아하는 음식 top 3:", foods[:3])

toRemove = input("지우고 싶은 음식: ")
foods.remove(toRemove)
print("결과:", foods)