import re
from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_year(value):
    now = timezone.now().year
    if value > now:
        raise ValidationError(
            ('Введенный вами год %(value)s не может быть больше текущего!'),
            params={'value': value},
        )


def validate_username(value):
    if value.lower() == 'me':
        raise ValidationError(
            'Не допустимое имя пользователя.'
        )
    if not re.match(r'^[\w.@+-]+\Z', value):
        raise ValidationError(
            f'Не допустимые символы <{value}> в нике.'
        )
    return value
