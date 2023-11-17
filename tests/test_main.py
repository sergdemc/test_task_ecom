from service.main import handle_request


def test_generate_response_404():
    request = 'GET /unknown HTTP/1.1\nHost: localhost\n\n'
    expected_response = b'HTTP/1.1 404 Not found\n\n{"error": "404 Not found"}'
    response = handle_request(request)
    assert response == expected_response


def test_generate_response_405():
    request = 'GET /get_form HTTP/1.1\nHost: localhost\n\n'
    expected_response = b'HTTP/1.1 405 Method not allowed\n\n{"error": "405 Method not allowed"}'
    response = handle_request(request)
    assert response == expected_response
