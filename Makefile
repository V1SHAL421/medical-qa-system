.PHONY: run test install lint

run:
	python src/main.py

test:
	pytest tests/

lint:
	ruff check .
	ruff format .

install:
	pip install -r requirements.txt