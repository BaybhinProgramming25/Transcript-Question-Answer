# Start everything
up:
	docker compose up -d --build

# Stop everything
down:
	docker compose down

# Restart everything
restart:
	docker compose down
	docker compose up -d --build

# Visit logs
logs:
	docker compose logs -f