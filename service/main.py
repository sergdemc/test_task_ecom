import json
import socket

from service.db import init_db
from service.utils import parse_request
from service.views import get_form

URLS = {
    '/get_form': get_form,
}

ALLOWED_METHODS = ['POST',]


def generate_headers(method, url) -> tuple[str, int]:
    if url not in URLS:
        return 'HTTP/1.1 404 Not found\n\n', 404

    if method not in ALLOWED_METHODS:
        return 'HTTP/1.1 405 Method not allowed\n\n', 405

    return 'HTTP/1.1 200 OK\n\n', 200


def generate_content(request, code, url) -> str | dict:
    if code == 404:
        return json.dumps({'error': '404 Not found'})
    if code == 405:
        return json.dumps({'error': '405 Method not allowed'})

    return URLS[url](request)  # get_form()


def handle_request(request) -> bytes:
    method, url = parse_request(request)
    headers, code = generate_headers(method, url)
    body = generate_content(request, code, url)
    body = json.dumps(body) if isinstance(body, dict) else body
    return (headers + body).encode('utf-8')


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', 5001))
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        print(request)

        response = handle_request(request.decode('utf-8'))

        client_socket.sendall(response)
        client_socket.close()


if __name__ == '__main__':
    init_db()
    run()
