firstNum = int(input())
secondNum = int(input())
thirdNum = int(input())

# if firstNum > secondNum and firstNum > thirdNum:
#     print(firstNum)
# elif firstNum < secondNum :
#     print(secondNum)
# else:
#     print(thirdNum)

number = 0
if firstNum > secondNum:
    number = firstNum
else:
    number = secondNum
if number > thirdNum:
    print(number)
else:
    print(thirdNum)
