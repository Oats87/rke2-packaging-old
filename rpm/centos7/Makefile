COMMIT ?= $(shell git rev-parse HEAD)

build:
	TAG=${TAG} \
	$(MAKE) build-common
	TAG=${TAG} \
	$(MAKE) build-server
	TAG=${TAG} \
	$(MAKE) build-agent

build-common:
	mkdir -p ./dist
	DOCKER_BUILDKIT=1 \
	docker build \
	    -f Dockerfile.common \
		--build-arg TAG=${TAG} \
		--build-arg COMMIT=${COMMIT} \
		-o ./dist .

build-server:
	mkdir -p ./dist
	DOCKER_BUILDKIT=1 \
	docker build \
	    -f Dockerfile.server \
		--build-arg TAG=${TAG} \
		--build-arg COMMIT=${COMMIT} \
		-o ./dist .

build-agent:
	mkdir -p ./dist
	DOCKER_BUILDKIT=1 \
	docker build \
	    -f Dockerfile.agent \
		--build-arg TAG=${TAG} \
		--build-arg COMMIT=${COMMIT} \
		-o ./dist .