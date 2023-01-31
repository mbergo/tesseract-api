VENV_NAME=venv
PYTHON=python3

all: build

build: venv requirements.txt templates

venv:
	virtualenv -p $(PYTHON) $(VENV_NAME)

requirements.txt:
	$(VENV_NAME)/bin/pip install -r requirements.txt

templates:
	mkdir -p templates
	mkdir -p images
run: venv
	export FLASK_APP=app.py; \
	flask run --port 8080 --debugger

