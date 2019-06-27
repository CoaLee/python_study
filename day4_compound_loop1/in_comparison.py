# is_in_comparison.py

primeNumbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

print(2 in primeNumbers)
print(12 in primeNumbers)

inputNum = int(input("30 이하의 자연수를 입력해주세요: "))
isPrime = False

if inputNum > 30 or inputNum < 1:
    print("잘못된 입력입니다")
else:
    if inputNum in primeNumbers:
        isPrime = True

    if isPrime is True:
        print(inputNum + ": 소수입니다")
    else: 
        print(inputNum + ": 소수가 아닙니다")