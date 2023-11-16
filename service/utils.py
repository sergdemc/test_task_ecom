import copy
import json
from db import db
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


def annotype_body(data: dict) -> dict:
    validated_data = copy.deepcopy(data)
    for key, value in validated_data.items():
        validated_data[key] = validate_value(str(value))
    return validated_data


def get_forms():
    try:
        forms = [el for el in db.forms.find({}, {'_id': 0})]
        return forms
    except Exception as e:
        print(f"Ошибка при получении документов: {e}")
        return None


def find_form(body: dict) -> str | dict:
    result = []
    forms = get_forms()
    print(forms)
    for form in forms:
        form_name = form.pop('name')
        if all(item in body.items() for item in form.items()):
            unmatched_fields = len(body.keys() - form.keys())
            result.append((unmatched_fields, form_name))
    if not result:
        return body
    return min(result)[1]
