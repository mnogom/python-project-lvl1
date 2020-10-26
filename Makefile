install:
	poetry install


brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even


build:
	poetry build

package-install:
	pip3 install --user --upgrade dist/*.whl

lint:
	poetry run flake8 brain_games
