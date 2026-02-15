import re

from rest_framework.serializers import ValidationError

from utils import regex_patterns as rgx


def is_exist(obj, field_name: str, value: str, cls):
    qs = cls.objects.filter(**{f'{field_name}__iexact': value})

    if getattr(obj, 'instance', None): qs = qs.exclude(id=obj.instance.id)

    if qs.exists(): raise ValidationError(f'{cls.__name__.lower()} with this {field_name} already exists.')


def contains_english_letter(word: str, field_name: str):
    if not re.match(rgx.ENGLISH_LETTER, word):
        raise ValidationError(f'{field_name} must contain only English letters and spaces.')
