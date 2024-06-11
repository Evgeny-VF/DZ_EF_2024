#Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."
first=input("Введите первое число 'first': ")
two=input("Введите второе число 'two': ")
third=input("Введите третье число 'third': ")
if first == two :
    if two==third:
        print("Число 'first'- ",first, " равно числу 'two'- ", two, "и равно числу 'third'- ", third, ", значит результат = ", 3)
    else:
        print("Число 'first'- ", first, " равно числу 'two'- ", two, "и НЕ равно числу 'third'- ", third, ", значит результат = ", 2)
elif two==third:
    print("Число 'first'- ", first, " НЕ равно числу 'two'- ", two, ", а число 'two'- ", two, " равно числу 'third'-  ", third, ", значит результат = ", 2)
elif first==third:
    print("Число 'first'- ", first, " НЕ равно числу 'two'- ", two, "и  равно числу 'third'-  ", third, ", значит результат = ", 2)
else:
        print("Число 'first'- ", first, " НЕ равно числу 'two'- ", two, ", а число 'two'- ", two, " НЕ равно числу 'third'-  ",  third, ", значит результат = ", 0)