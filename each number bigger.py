# Даны два целых числа. Программа должна вывести число "1",
# если первое число больше второго,
#  число "2", если второе больше первого или число "0", если они равны.
firstNum = int(input())
secondNum = int(input())

if firstNum > secondNum:
    print(1)
elif secondNum > firstNum:
    print(2)
else:
    print(0)
