#  Домашняя работа по уроку "Стиль кода часть II. Цикл While."
my_list = my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
_listIndex = 0
_trigger = 0
while int(_listIndex) != int(len(my_list)):
    while _listIndex <= int(len(my_list)) - 1:
        if my_list[_listIndex] > 0:
            print(my_list[_listIndex])
            _listIndex = _listIndex + 1
        elif my_list[_listIndex] < 0:
            break
        elif my_list[_listIndex] == 0:
            _listIndex = _listIndex + 1
            continue
        if (int(len(my_list)) - int(_listIndex) - 1) == -1:
            print('Проверка списка завершена.')
        elif  int(my_list[_listIndex]) < 0:
            print('Количество неидентифицированных элементов списка =  ', int(len(my_list)) - int(_listIndex) - 1)
    if (int(len(my_list)) - int(_listIndex) - 1) != -1:
        _trigger = input('Продолжить -"1", завершить - любой иной символ.')
        if int(_trigger) == 1:
            _listIndex = _listIndex + 1
            continue
         else:
            print('Проверка списка завершена.')
            break
