import pytest
from service.utils import (
    parse_body,
    parse_request,
    validate_value,
    annotype_body,
    get_forms,
    find_form
)


@pytest.fixture
def example_request():
    return ("GET /some_url HTTP/1.1\r\nHost: localhost\r\nContent-Type: application/json\r\n\r\n{\"field1\": "
            "\"value1\", \"field2\": \"value2\"}")


def test_parse_body():
    request = ("POST /some_url HTTP/1.1\r\nHost: localhost\r\nContent-Type: application/json\r\n\r\n{\"field1\": "
               "\"value1\", \"field2\": \"value2\"}")
    expected_output = {"field1": "value1", "field2": "value2"}
    assert parse_body(request) == expected_output


def test_parse_request():
    request = "GET /some_url HTTP/1.1\r\nHost: localhost\r\n\r\n"
    method, url = parse_request(request)
    assert method == "GET"
    assert url == "/some_url"


def test_validate_value():
    assert validate_value("2023-11-16") == "date"
    assert validate_value("+79991112233") == "phone"
    assert validate_value("test@example.com") == "email"
    assert validate_value("some text") == "text"


def test_annotype_body():
    data = {"field1": "2023-11-16", "field2": "+79991112233", "field3": "test@example.com", "field4": "some text"}
    expected_output = {"field1": "date", "field2": "phone", "field3": "email", "field4": "text"}
    assert annotype_body(data) == expected_output


def test_get_forms():
    forms = [
        {'name': 'User profile', 'username': 'text', 'phone': 'phone', 'lead_email': 'email', 'created_at': 'date'},
        {'name': 'Order', 'username': 'text', 'description': 'text', 'created_at': 'date'},
        {'name': 'Support ticket', 'ticket': 'text', 'created_at': 'date'},
        {'name': 'SOS', 'sos_phone': 'phone', 'sos_email': 'email'}
    ]
    assert len(get_forms()) == len(forms)


def test_find_form():
    body = {'sos_phone': 'phone', 'sos_email': 'email'}
    result = find_form(body)
    assert result == 'SOS'
