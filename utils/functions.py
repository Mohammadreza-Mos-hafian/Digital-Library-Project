from typing import Any

from rest_framework.serializers import ValidationError


def name_exists(obj: Any, field_name: str, value: str, cls):
    exists = cls.objects.filter(name__iexact=value).exclude(id=obj.instance.id if obj.instance else None).exists()

    if exists:
        raise ValidationError(f'{field_name} with this name already exists.')
