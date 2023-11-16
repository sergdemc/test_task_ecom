from utils import parse_body, annotype_body
from utils import find_form
import json


def get_form(request):
    body = parse_body(request)

    if 'error' in body:
        return json.dumps(body)

    annotyped_body = annotype_body(body)
    data = find_form(annotyped_body)
    return data
