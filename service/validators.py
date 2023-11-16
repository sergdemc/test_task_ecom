import re


def validate_email(email: str) -> bool:
    email_pattern = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')  # noqa
    return bool(email_pattern.fullmatch(email))


def validate_phone(phone: str) -> bool:
    phone_pattern = re.compile(r'\+7\d{10}')
    return bool(phone_pattern.fullmatch(phone))


def validate_date(date_string: str) -> bool:
    date_pattern = re.compile(r'^(\d{2}\.\d{2}\.\d{4}|\d{4}-\d{2}-\d{2})$')
    return bool(date_pattern.match(date_string))
