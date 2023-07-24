DC=cd docker && docker-compose

.PHONY: build
build: #Build project
build:
	@${DC} build

.PHONY: server
server: #Serve project
server:
	@${DC} up

.PHONY: add
add: #Poetry add package
add:
	@${DC} run --no-deps myfinance poetry add $(package)

.PHONY: remove
remove: #Poetry remove package
remove:
	@${DC} run --no-deps myfinance poetry remove $(package)
