def is_integer(x):
    if isinstance(x, (int, float)):
        return float(x).is_integer()
    raise TypeError()


val_1 = input('Введите число из первой вставки: ')
result_ = []
for i in range(1, int(val_1) + 1):
    for j in range(i+1, int(val_1) + 1):
        flag_1 = is_integer(int(val_1) / (i+j))
        if  flag_1:
            prom_ = str(i) + str(j)
            result_.append(prom_)
print(*(result_))
