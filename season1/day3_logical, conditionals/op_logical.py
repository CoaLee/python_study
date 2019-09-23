# op_logical.py

numA = 38
numB = -9
numC = 50

print(numA > numB)  # True? False?
print(numB < numC)  # True? False?
print(numA > numB and numB < numC)      # and 활용  # True? False?
print(numA > numB or numB < numC)       # or 활용   # True? False?
print(not (numA > numB))                # not 활용  # True? False?
print(not (numA > numB) and numB < numC)    # 섞어서 활용   # True? False?

# 변수를 활용한 형식으로 바꾸면?




















boolA = numA > numB
boolB = numB < numC
print(boolA)
print(boolB)
print(boolA and boolB)
print(boolA or boolB)
print(not boolA)
print(not boolA and boolB)

