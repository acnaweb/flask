export IMAGE_NAME=flask

# Local development
install:
	python -m venv venv; \
	. venv/bin/activate; \
	pip install --upgrade pip; \
	pip install pre-commit; \
	pip install -e .[interactive]; \
	pre-commit install; \
	git config --bool flake8.strict true; \

formatter:
	black src
	
typing: formatter
	mypy src

lint:
	flake8  src

build:
	python setup.py install

test:
	pytest

# Containter

c_build:
	docker build -t ${IMAGE_NAME} .

c_run:
	if [ ! -f .env ]; then \
		docker run -d -p 5000:5000 ${IMAGE_NAME}; \
	else \
		docker run --env-file .env -d ${IMAGE_NAME}; \
	fi

debug:
	flask --app src/app run --host=0.0.0.0 --debug
	
run:
	flask --app src/app run --host=0.0.0.0 
