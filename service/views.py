from utils import parse_body, validate_body
import json
import copy


def get_form(request):
    body = parse_body(request)

    if 'error' in body:
        return json.dumps(body)

    validated_body = validate_body(body)

    return json.dumps(validated_body)
