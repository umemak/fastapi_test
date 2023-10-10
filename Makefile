
.PHONY: up
up:
	docker compose up -d

.PHONY: down
down:
	docker compose down

.PHONY: migrate
migrate:
	docker compose run --entrypoint "poetry run python -m api.migrate_db" demo-app

.PHONY: test
test:
	docker compose run --entrypoint "poetry run pytest" demo-app
