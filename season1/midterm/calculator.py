# midterm exercise

print("\nHello from Vietnam! ")
print("못 봐서 아쉽네요. 중간 과제를 드립니다. 아래 계산 기능(1~3)을 하나씩 구현해보세요 :)")
print("\n=== 하랑 계산기 버전 선택 ===")
print("| 0: 순서대로 모두 보기    |")
print("| 1: 덧셈 연산 계산기(0.1) |")
print("| 2: 사칙 연산 계산기(0.2) |")
print("| 3: 입력 연산 계산기(0.3) |")
print()
cmd = input("> 원하는 번호를 입력하세요(0~3): ")

if cmd == "1":
    # First step
    print("\n\n--- 하랑 계산기 Ver 0.1: 덧셈 연산 계산기 ---")
    print("Input: 계산할 수 두개")
    print("Output: 덧셈 연산 결과(+)\n")

    strA = input("> first number: ")
    strB = input("> second number: ")

    numA = int(strA)
    numB = int(strB)

    print("\n[ Result ]")
    print(strA + " + " + strB + " = " + str(numA + numB))
elif cmd == "2":
    # Second step
    print("\n\n--- 하랑 계산기 Ver 0.2: 사칙 연산 계산기 ---")
    print("Input: 계산할 수 두개")
    print("Output: 사칙연산 결과(+, -, *, /)\n")

    strA = input("> first number: ")
    strB = input("> second number: ")

    numA = int(strA)
    numB = int(strB)

    print("\n[ Result ]")
    print(strA + " + " + strB + " = " + str(numA + numB))
    print(strA + " - " + strB + " = " + str(numA - numB))
    print(strA + " * " + strB + " = " + str(numA * numB))

    if numB != 0:
        print(strA + " / " + strB + " = " + str(numA / numB))
    else:
        print("Error!")
elif cmd == "3":
    # Third step
    print("\n\n--- 하랑 계산기 Ver 0.3: 입력 연산 계산기 ---")
    print("Input: 계산할 수 두개와 연산자 하나")
    print("Output: 입력한 연산자 연산 결과\n")

    strA = input("> first number: ")
    op = input("> operator (+, -, *, /): ")
    strB = input("> second number: ")

    numA = int(strA)
    numB = int(strB)

    isValid = True
    result = 0

    if op == "+":
        result = numA + numB
    elif op == "-":
        result = numA - numB
    elif op == "*":
        result = numA * numB
    elif op == "/":
        if numB != 0:
            result = numA / numB
        else:
            isValid = False
    else:
        isValid = False

    print("\n[ Result ]")
    if isValid:
        print(strA + " " + op + " " + strB + " = " + str(result))
    else:
        print("Error!")
elif cmd == "0":
    # First step
    print("\n\n--- 하랑 계산기 Ver 0.1: 덧셈 연산 계산기 ---")
    print("Input: 계산할 수 두개")
    print("Output: 덧셈 연산 결과(+)\n")

    strA = input("> first number: ")
    strB = input("> second number: ")

    numA = int(strA)
    numB = int(strB)

    print("\n[ Result ]")
    print(strA + " + " + strB + " = " + str(numA + numB))


    # Second step
    print("\n\n--- 하랑 계산기 Ver 0.2: 사칙 연산 계산기 ---")
    print("Input: 계산할 수 두개")
    print("Output: 사칙연산 결과(+, -, *, /)\n")

    strA = input("> first number: ")
    strB = input("> second number: ")

    numA = int(strA)
    numB = int(strB)

    print("\n[ Result ]")
    print(strA + " + " + strB + " = " + str(numA + numB))
    print(strA + " - " + strB + " = " + str(numA - numB))
    print(strA + " * " + strB + " = " + str(numA * numB))

    if numB != 0:
        print(strA + " / " + strB + " = " + str(numA / numB))
    else:
        print("Error!")


    # Third step
    print("\n\n--- 하랑 계산기 Ver 0.3: 입력 연산 계산기 ---")
    print("Input: 계산할 수 두개와 연산자 하나")
    print("Output: 입력한 연산자 연산 결과\n")

    strA = input("> first number: ")
    op = input("> operator (+, -, *, /): ")
    strB = input("> second number: ")

    numA = int(strA)
    numB = int(strB)

    isValid = True
    result = 0

    if op == "+":
        result = numA + numB
    elif op == "-":
        result = numA - numB
    elif op == "*":
        result = numA * numB
    elif op == "/":
        if numB != 0:
            result = numA / numB
        else:
            isValid = False
    else:
        isValid = False

    print("\n[ Result ]")
    if isValid:
        print(strA + " " + op + " " + strB + " = " + str(result))
    else:
        print("Error!")
elif cmd == "hint":
    print("\n[hint] 사용한 함수 / 키워드: print(), input(), int(), str(), if, elif, else")
    print("간단한 힌트입니다. 파이팅!")
else:
    print("번호의 범위는 0~3 입니다. 힌트를 원하면 hint라고 입력해보세요.")