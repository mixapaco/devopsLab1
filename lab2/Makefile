.DEFAULT_GOAL := all

all: install test run deploy

install:
	@echo "Installing pipenv and dependencies.";
	python3 -m pip install pipenv;	 	
	python3 -m pipenv --python 3.9;
	
	
	python3 -m pipenv install requests;
	python3 -m pipenv install ntplib;

	python3 -m pipenv install pytest;	

test:
	@echo "Start tests.";
	python3 -m pipenv run pytest ./tests/tests.py > results.txt;

run:
	@echo "Run Python app."
	python3 -m pipenv run python app.py > results.txt

deploy:
	@echo "Adding and Committing results.txt to git.";
	python3 -m pipenv run pytest ./tests/tests.py > results.txt; python3 -m pipenv run python app.py >> results.txt
	git add ./results.txt;
	git commit -m "Lab2: deploy through make";
	git push origin main
	
test-cli:
	pipenv run pytest tests/tests.py