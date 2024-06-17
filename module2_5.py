# Домашняя работа по уроку "Функции в Python.Функция с параметром"
def get_matrix(n, m, value):
    prom_ = []
    matrix_ = []
    for i in range(1, int(n) + 1):
        prom_.append(value)
    for j in range(1, int(m) + 1):
        matrix_.append(prom_)
    return n, m, value, matrix_


r1 = get_matrix(2, 2, 10)
r2 = get_matrix(3, 5, 42)
r3 = get_matrix(4, 2, 13)
print('get_mstrix'+ str(r1)[0:int(str(r1).find('[')) - 2] + ') = ' + str(r1)[int(str(r1).find('[')):len(str(r1)) - 1])
print('get_mstrix'+ str(r2)[0:int(str(r2).find('[')) - 2] + ') = ' + str(r2)[int(str(r2).find('[')):len(str(r2)) - 1])
print('get_mstrix'+ str(r3)[0:int(str(r3).find('[')) - 2] + ') = ' + str(r3)[int(str(r3).find('[')):len(str(r3)) - 1])
