from service.views import get_form


def test_get_form_success():
    request = ('POST /get_form HTTP/1.1\r\nHost: localhost:5001\r\nUser-Agent: '
               'python-requests/2.31.0\r\nAccept-Encoding: gzip, deflate\r\nAccept: */*\r\nConnection: '
               'keep-alive\r\nContent-Length: 106\r\nContent-Type: application/json\r\n\r\n{"username": "Admin", '
               '"phone": "+79997775533", "lead_email": "admin@admin.ru", "created_at": "2000-05-12"}')

    data = get_form(request)
    expected_data = 'User profile'
    assert data == expected_data


def test_get_form_unsuccess():
    request = ('POST /get_form HTTP/1.1\r\nHost: localhost:5001\r\nUser-Agent: '
               'python-requests/2.31.0\r\nAccept-Encoding: gzip, deflate\r\nAccept: */*\r\nConnection: '
               'keep-alive\r\nContent-Length: 106\r\nContent-Type: application/json\r\n\r\n{"customer": "GazMyas", '
               '"phone": "+79997775533", "lead_email": "admin@admin.ru", "created_at": "2000-05-12"}')

    data = get_form(request)
    expected_data = {
        "customer": "text",
        "phone": "phone",
        "lead_email": "email",
        "created_at": "date"
    }
    assert data == expected_data
