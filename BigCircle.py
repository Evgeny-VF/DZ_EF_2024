# Домашняя работа по уроку "Пространство имен."
def test_func():# Создайте новую функцию def test_function
    def inner_funk():
        def drugaya_funk(): # Создайте другую функцию внутри функции inner_function
            _text = 'Я в области видимости функции test_function' # "Эта функция должна печатать текст "Я в области видимости функции test_function"
            return _text
        _text = drugaya_funk()
        return _text
    _text = inner_funk()#Вызовите функцию inner_function внутри функции test_function
    return _text


print(test_function())
print(inner_funk())#Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы

