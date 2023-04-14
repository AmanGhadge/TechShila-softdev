build:
	docker build --force-rm $(options) -t mosync:latest .

compose-start:
	docker-compose up --remove-orphans $(options)

compose-stop:
	docker-compose down --remove-orphans $(options)
