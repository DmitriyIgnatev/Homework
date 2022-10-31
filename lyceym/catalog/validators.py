def validate_amazing(value):
    value = set(value.lower().split())
    the_same = set(('превосходно', 'роскошно')) & value
    if not the_same:
        raise ValueError(
            'Обязательно нужно использовать строки превосходно или роскошно'
            )
    return value


def validate_number(value):
    if 0 > value > 32767:
        raise ValueError('Число должно быть больше нуля, меньше 32767')
    return value


def validate_word(value):
    # if [',', '!', '&', '?', '/', '.', ';', ':'] in value:
    #     raise ValueError(
    #         'Можно использовать только цифры,
    #  буквы латиницы и символы - и _')
    return value
