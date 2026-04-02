from typing import Optional
from wtforms import ValidationError
from flask_wtf import FlaskForm
from wtforms import Field

def number_length(min: int, max: int, message: Optional[str] = None):
    message = message or f"Номер должен иметь {min}-{max} цифр."

    def _number_length(form: FlaskForm, field: Field):
        value = field.data
        if value is not None and not isinstance(value, (int, float)):
            raise ValidationError
        value_str = str(value)
        length = len(value_str)

        if length < min or length > max:
            raise ValidationError(message)

    return _number_length

class NumberLength:
    def __init__(self, min: int, max: int, message: Optional[str] = None):
        self.min_digits = min
        self.max_digits = max
        self.message = message or f"Номер должен иметь {min}-{max} цифр."

    def __call__(self, form: FlaskForm, field: Field):
        value = field.data
        if value is not None and not isinstance(value, (int, float)):
            raise ValidationError

        value_str = str(value)
        length = len(value_str)

        if length < self.min_digits or length > self.max_digits:
            raise ValidationError(self.message)