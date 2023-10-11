DC=cd docker && docker-compose
CODE=my_finance

include ./makefiles/test.mk

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

.PHONY: dev-add
dev-add: #Poetry add package
dev-add:
	@${DC} run --no-deps myfinance poetry add --group dev $(package)

.PHONY: remove
remove: #Poetry remove package
remove:
	@${DC} run --no-deps myfinance poetry remove $(package)


.PHONY: migration
migration: #alembic make revision
migration:
	@${DC} run --no-deps myfinance poetry run alembic revision --autogenerate -m "$(message)"
