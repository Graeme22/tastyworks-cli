.PHONY: clean venv test

clean:
	find . -name '*.py[co]' -delete

venv:
	python -m venv --prompt 'twcli' env
	env/bin/pip install -r requirements.txt
	env/bin/pip install -r requirements-dev.txt
	env/bin/python setup.py develop

test:
	isort --check --diff twcli/ tests/
	flake8 --count --show-source --statistics twcli/ tests/
	pytest --cov=twcli --cov-report=term-missing tests/
