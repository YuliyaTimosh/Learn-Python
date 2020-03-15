# Для данного числа n<100 закончите фразу “На лугу пасется...”
# одним из возможных продолжений: “n коров”, “n корова”,
#  “n коровы”, правильно склоняя слово “корова”.
# Программа должна вывести введенное число n и одно из
# слов: korov, korova или korovy.
#  Между числом и словом должен стоять ровно один пробел.

numberOfCow = int(input())

if numberOfCow // 10 == 1:
    print(numberOfCow, 'korov')
elif numberOfCow % 10 == 1:
    print(numberOfCow, 'korova')
elif numberOfCow % 10 >= 2 and numberOfCow % 10 <= 4:
    print(numberOfCow, 'korovy')
else:
    print(numberOfCow, 'korov')
