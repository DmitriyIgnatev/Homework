from django.core.exceptions import ValidationError


class Validate_amazing:
    def __init__(self, *base):
        self.base = base

    def __call__(self, value):
        flag_for_validation = True
        signs = r'!\"№;%:?*()_+=-?><,:"/'
        for word in value.split():
            for important_word in self.base:
                if important_word.lower() == word.lower().strip(signs + "'"):
                    flag_for_validation = False
                    break
        if flag_for_validation:
            message = f'Должны быть слова: {", ".join(list(self.base))}'
            raise ValidationError(message)
        return value


def validate_number(value):
    if 0 > value > 32767:
        raise ValidationError('Число должно быть больше нуля, меньше 32767')
    return value


def validate_word(value):
    text = 'Можно использовать только цифры, буквы латиницы и символы - и _'
    letters = [',', '!', '&', '?', '/', '.', ';', ':']
    for word in value.split():
        for letter in letters:
            if letter in word:
                raise ValidationError(text)
    return value
