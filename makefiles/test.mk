.PHONY: black
black: #Poetry add package
black:
	@${DC} run --no-deps myfinance poetry run black ${CODE}

.PHONY: flake8
flake8: #Poetry add package
flake8:
	@${DC} run --no-deps myfinance poetry run flake8 ${CODE}

.PHONY: isort
isort: #Poetry add package
isort:
	@${DC} run --no-deps myfinance poetry run isort ${CODE}
