start-mongo:
	docker rm -f my-mongo || true
	docker run --name my-mongo -p 27017:27017 -d mongodb/mongodb-community-server:latest

stop-mongo:
	docker stop my-mongo

server:
	python3 -m service.main

start:
	make start-mongo
	make server

requirements:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

test:
	python3 -m service.tests -v

venv:
	python3 -m venv venv && source venv/bin/activate

install:
	python3 pip install -r requirements.txt

check:
	flake8 service && isort service
