from django.core.exceptions import ValidationError
import re
from django.utils.deconstruct import deconstructible


@deconstructible
class Validate_amazing:
    def __init__(self, *base):
        self.base = '|'.join(list(base))

    def __call__(self, value):
        flag_for_validation = True
        if re.search(re.compile(fr'\b({self.base})\b', re.I), value):
            flag_for_validation = False
        if flag_for_validation:
            message = f'Должны быть слова: {", ".join(self.base.split("|"))}'
            raise ValidationError(message)
        return value


def validate_number(value):
    if 0 > value > 32767:
        raise ValidationError('Число должно быть больше нуля, меньше 32767')
    return value
