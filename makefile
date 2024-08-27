.PHONY: start
start: build up 

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

clean:
	docker-compose down --rmi all --volumes --remove-orphans
