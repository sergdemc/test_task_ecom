import copy
import json
from validators import validate_email, validate_phone, validate_date

VALIDATORS = {
    'date': validate_date,
    'phone': validate_phone,
    'email': validate_email,
    'text': lambda value: True
}


def parse_body(request) -> dict:
    request_parts = request.split('\r\n\r\n')
    body = request_parts[1]

    try:
        body_dict = json.loads(body)
        return body_dict
    except json.JSONDecodeError as e:
        print("Ошибка декодирования JSON:", e)
        return {'error': f'JSONDecodeError: {e}'}


def parse_request(request):
    parsed = request.split(' ')
    method = parsed[0]
    url = parsed[1]
    return method, url


def validate_value(value: str) -> str:
    for key, validator in VALIDATORS.items():
        if validator(value):
            return key


def validate_body(data: dict) -> dict:
    validated_data = copy.deepcopy(data)
    for key, value in validated_data.items():
        validated_data[key] = validate_value(value)
    return validated_data
