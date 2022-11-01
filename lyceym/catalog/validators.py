from django.core.exceptions import ValidationError


class Validate_amazing:
    def __init__(self, *base):
        self.base = set(base)

    def __call__(self, value):
        if not set(value.lower().split()) & self.base:
            message = f'Должны быть слова: {", ".join(list(self.base))}'
            raise ValidationError(message)
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
