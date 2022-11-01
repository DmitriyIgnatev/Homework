from django.core.exceptions import ValidationError


def validate_amazing(value):
    value = set(value.lower().split())
    the_same = set(('превосходно', 'роскошно')) & value
    if not the_same:
        raise ValidationError(
            'Обязательно нужно использовать строки превосходно или роскошно'
            )
    return value


def validate_number(value):
    if 0 > value > 32767:
        raise ValidationError('Число должно быть больше нуля, меньше 32767')
    return value


def validate_word(value):
    text = 'Можно использовать только цифры, буквы латиницы и символы - и _'
    sets = {',', '!', '&', '?', '/', '.', ';', ':'}
    for i in value.split():
        if set(i) & sets:
            raise ValidationError(text)
    return value
