# Практческое задание по теме Неизменяемые и изменяемые объекты
immutable_var='Пешеход', 'Велосипедист', 'Автомобилист',  'Лётчик'
print('Это кортеж: ', immutable_var)
_prom=input("Какой номер из кортежа 'immutable_var' распечатать?")
#nomer_vk=_prom
#print(immutable_var[int(_prom)])
_prom=immutable_var[int(_prom)]
print(_prom)
Mutable_list=['Пешеход', 'Велосипедист', 'Автомобилист',  'Лётчик' ]
print('Это список: ',Mutable_list)
print('Объём кортежа = ', immutable_var.__sizeof__(),', объём списка = ', Mutable_list.__sizeof__(),'.')
_prom=input('Какое слово добавить в кортеж и список?')
Mutable_list.append(_prom)
immutable_var=immutable_var+(_prom,)
print('Это кортеж: ', immutable_var,', объём кортежа = ', immutable_var.__sizeof__(),'.' )
print('Это список: ', Mutable_list,', объём списка = ', Mutable_list.__sizeof__(),'.')
_minusKort=input('Какое слово удалить из кортежа?')
_idxKort=immutable_var.index(str(_minusKort))
immutable_var=immutable_var[:_idxKort]+immutable_var[_idxKort+1:]
_minusSps=input('Какое слово удалить из списка?')
Mutable_list.remove(_minusSps)
print('Immutable_var: ',immutable_var)
print('Mutable_list: ',Mutable_list)