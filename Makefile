start-mongo:
	docker rm -f my-mongo || true
	docker run --name my-mongo -p 27017:27017 -d mongodb/mongodb-community-server:latest

stop-mongo:
	docker stop my-mongo

create-db:
	docker exec -it my-mongo mongo my_database --eval "db.createCollection('forms')"

import-data:
	docker exec -it my-mongo mongoimport --db my_database --collection forms --file db_data.json --jsonArray

