import re

from typing import Any

from rest_framework.serializers import ValidationError

from utils import regex_patterns as rgx


def name_exists(obj: Any, value: str, cls):
    exists = cls.objects.filter(name__iexact=value).exclude(id=obj.instance.id if obj.instance else None).exists()

    if exists:
        raise ValidationError(f'{cls.__name__.lower()} with this name already exists.')


def contains_english_letter(word: str, field_name: str):
    if not re.match(rgx.ENGLISH_LETTER, word):
        raise ValidationError(f'{field_name} must contain only English letters and spaces.')
