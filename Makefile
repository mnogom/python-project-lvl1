install:
	poetry install


brain-games:
	poetry run brain-games

build:
	poetry build

package-install:
	pip3 install --user --upgrade dist/*.whl

lint:
	poetry run flake8 brain_games
