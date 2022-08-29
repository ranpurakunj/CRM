from rest_framework import serializers

import phonenumbers

from .models import Profile

def phone_validator(value):
    if not phonenumbers.is_possible_number(value):
        raise serializers.ValidationError(f"{value} doesn't seem to be a right number")
    return value
