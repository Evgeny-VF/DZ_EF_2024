def kapusta(*args):
    summa_ = 0
    for kochan in args:
        if isinstance(kochan, list):
            for listok in kochan:
                summa_ += kapusta(listok )
        elif isinstance(kochan, tuple):
            for listok  in kochan:
                summa_ += kapusta(listok )
        elif isinstance(kochan, set):
            for listok  in kochan:
                summa_ += kapusta(listok )
        elif isinstance(kochan, dict):
            for key, value in kochan.items():
                summa_ += kapusta(key, value)
        elif isinstance(kochan, str):
            summa_ += len(kochan)
        elif isinstance(kochan, int):
            summa_ += kochan
    return summa_


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result_ = kapusta(data_structure)
print('Сумма цифр и количества букв в data_structure = ',result_)