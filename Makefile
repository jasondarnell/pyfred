

test:
	pytest --cov=pyfred --cov-report xml --cov-report term  --cov-report html tests
	flake8 pyfred
	flake8 tests


lint:
	flake8 pyfred
	flake8 tests
