from typing import Any

from rest_framework.serializers import ValidationError


def name_exists(obj: Any, value: str, cls):
    exists = cls.objects.filter(name__iexact=value).exclude(id=obj.instance.id if obj.instance else None).exists()

    if exists:
        raise ValidationError(f'{cls.__name__.lower()} with this name already exists.')
