# Напишите функцию принимающую на вход только
# ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента,
# а значение — имя аргумента.
# Если ключ не хешируем, используйте
# его строковое представление.

def get_key_dict(**kwargs):
    temp_dict = dict()

    for key, value in kwargs.items():
        try:
            n = hash(value)
            temp_dict[value] = key
        except TypeError:
            temp_dict[str(value)] = key
    return temp_dict

print(get_key_dict(arg1="Hello",arg2=2,arg3="123",arg4=[1,2,3,4,5]))

