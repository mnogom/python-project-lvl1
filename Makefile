install:
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc

brain-gcd:
	poetry run brain-gcd

brain-progression:
	poetry run brain-progression

brain-prime:
	poetry run brain-prime

brain-hub:
	poetry run brain-hub

build:
	poetry build

package-install:
	pip3 install --user --upgrade dist/*.whl

lint:
	poetry run flake8 brain_games
