# Build the entire docker cluster
.PHONY: build
build: build-db

# Builds the db container
.PHONY: build-db
build-db:
	# mkdir -p ./database/assets;
	cd ./database; docker build --no-cache --build-arg DOCKER_POSTGRES_DB_PORT -t courier-db:latest .; cd ..;
