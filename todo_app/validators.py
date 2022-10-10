from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator

from todo_app import MIN_LENGTH, MAX_LENGTH


def min_length_validation(string):
    if len(string) < MIN_LENGTH:
        raise ValidationError(f"Make sure this field has more than {MIN_LENGTH} characters")


def max_length_validation(string):
    if len(string) > MAX_LENGTH:
        raise ValidationError(f"Make sure this field has less than {MAX_LENGTH} characters")

