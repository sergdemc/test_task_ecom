import json

from service.utils import annotype_body, find_form, parse_body


def get_form(request) -> str | dict:
    body = parse_body(request)

    if 'error' in body:
        return json.dumps(body)

    annotyped_body = annotype_body(body)
    data = find_form(annotyped_body)
    return data
