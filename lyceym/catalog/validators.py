from django.core.exceptions import ValidationError
import re
from django.utils.deconstruct import deconstructible


@deconstructible
class Validate_amazing:
    def __init__(self, *base):
        self.base = base

    def __call__(self, value):
        flag_for_validation = True
        for word in value.split():
            for important_word in self.base:
                word = word.lower()
                text = re.findall('[a-zа-яё]+', word, flags=re.IGNORECASE)
                try:
                    if important_word.lower() == text[0]:
                        flag_for_validation = False
                        break
                except IndexError:
                    continue
        if flag_for_validation:
            message = f'Должны быть слова: {", ".join(list(self.base))}'
            raise ValidationError(message)
        return value


def validate_number(value):
    if 0 > value > 32767:
        raise ValidationError('Число должно быть больше нуля, меньше 32767')
    return value
