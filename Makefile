start-mongo:
	docker rm -f my-mongo || true
	docker run --name my-mongo -p 27017:27017 -d mongodb/mongodb-community-server:latest

stop-mongo:
	docker stop my-mongo

server:
	python3 -m service.main

start:
	start-mongo
	server

requirements:
	poetry export -f requirements.txt --output requirements.txt

test:
	python3 -m service.tests -v



check:
	flake8 service && isort service