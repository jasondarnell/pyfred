

test:
	pytest --cov=pyfred --cov-report xml --cov-report term  --cov-report html tests
	make lint


lint:
	flake8 pyfred
	flake8 tests
