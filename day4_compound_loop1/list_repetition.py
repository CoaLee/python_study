# list_repetition.py

foods = []
print("좋아하는 음식 5개를 입력해 주세요.")

tmpFood = input("1번째 음식: ")
foods.append(tmpFood)

tmpFood = input("2번째 음식: ")
foods.append(tmpFood)

tmpFood = input("3번째 음식: ")
foods.append(tmpFood)

tmpFood = input("4번째 음식: ")
foods.append(tmpFood)

tmpFood = input("5번째 음식: ")
foods.append(tmpFood)

print("좋아하는 음식들:")
print(foods[0])
print(foods[1])
print(foods[2])
print(foods[3])
print(foods[4])

print("좋아하는 음식 top 3:", foods[:3])

toRemove = input("지우고 싶은 음식: ")
foods.remove(toRemove)