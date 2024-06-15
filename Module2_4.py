# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
test = []
primes = []
not_primes = []
for i in numbers:
    k = 0
    if i <= int(len(numbers)):
        for j in numbers:
            if j <= int(len(numbers)):
                test = numbers[i - 1] / numbers[j - 1]
                if len(str(test)) == 3:
                    if int(str(test)[2]) == 0:
                        k = k + 1
    if k <= 2:
        if i != 1:
            primes.append(i)
    else:
        not_primes.append(i)
print('Primes:', primes)
print('Not_primes:', not_primes)
