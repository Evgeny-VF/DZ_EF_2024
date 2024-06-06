# Практическое задание по теме"Словари и множества"
dikt_vendor={'Процессоры':100000001,'ОЗУ':1000000002,
            'Материнские платы':100000003, 'Жесткие диски':['HDD-2000','SSD-20002','SDD-20003']}
print("Содержание тестового словаря",dikt_vendor)
print('Все ключи словаря :',dikt_vendor.keys())
print('Все значения словаря :',dikt_vendor.values())
print('Все пары словаря :',dikt_vendor.items())
Name_ven=input('Введите имя продавца, чей номер надо вывести на экран: ')
print('Номер продавца "',Name_ven,'": ',dikt_vendor[Name_ven])
Name_ven=input('Введите имя продавца, чей номер надо изменить (если имя не будет найдено в словаре, то новая пара добавится в коней словаря: ')
New_num=input('Введите новый номер продавца: ')
dikt_vendor[Name_ven]=New_num
print('Содержание словаря после изменения :',dikt_vendor)#
Name_ven=input('Введите имя продавца, чью запись удалить #из справочника: ')
del dikt_vendor[Name_ven#]
print('Содержание словаря после удаления записи :',dikt_vendor)
New_dikt_ven={'Оперативная память':30003,'SSD':4004, 'Видеокарты':5005}
print('Дополнение к словарю:',New_dikt_ven)
dikt_vendor.update(New_dikt_ven)
print('Содержание словаря после объединения методом "Update":',dikt_vendor)
gradus_proc_set=28,32,43,65,66,70,45,23,33,66,28,23,43
print('Переменной "grad_proc_set" присвоено: ',gradus_proc_set)
gradus_proc_set=set(gradus_proc_set)
print('Переменная "grad_proc_set" конвертирована в множество: ',gradus_proc_set)
new_gradus=input('Введите значение температуры  для добавления в множество методом "add": ')
#new_gradus=set(new_gradus)
gradus_proc_set.add(int(new_gradus))
print('Содержание множества "grad_proc_set" после добавления: ',gradus_proc_set)
new_gradus=input('Введите значение температуры  для удаления из множества методом "discard": ')
gradus_proc_set.discard(int(new_gradus))
print('Содержание множества "grad_proc_set" после удаления: ',gradus_proc_set)
gradus_pop=gradus_proc_set.pop()
print('Из множества "grad_proc_set" извлекли произвольный элемент методом "pop": ',gradus_pop)
print('Содержание множества "grad_proc_set" после удаления: ',gradus_proc_set)