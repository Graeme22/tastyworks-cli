.PHONY: clean venv test dist dist-upload

clean:
	find . -name '*.py[co]' -delete

venv:
	python -m venv --prompt 'twcli' env
	env/bin/pip install -r requirements.txt
	env/bin/pip install -r requirements-dev.txt
	env/bin/python setup.py develop
	@echo "venv setup complete. Activate using: source env/bin/activate"

test:
	python -m pytest \
		-v \
		--cov=twcli \
		--cov-report=term \
		--cov-report=html:coverage-report \
		tests/

dist: clean
	rm -rf dist/*
	python setup.py sdist
	python setup.py bdist_wheel

dist-upload:
	twine upload dist/*
