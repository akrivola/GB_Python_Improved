# При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения аргументов и вызвать функцию

# При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения аргументов и вызовет функцию для проверки


def key_params(**kwargs):
    result = {}
    for value, key in kwargs.items():
        if key is None:
            key = 'None'
        try:
            result[key] =  value
        except:
            result[str(key)] = value

    return result


params = key_params(a=None, b='', c=[], d={})
print(params)
