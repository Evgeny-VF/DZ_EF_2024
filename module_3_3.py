# Самостоятельная работа по уроку "Распаковка параметров и параметры функции"
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
values_list = (67, 68, 'true')
print_params(*values_list)
dikt_ = {'a': 47, 'b': 38, 'c': 34}
print_params(**dikt_)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2,42)
