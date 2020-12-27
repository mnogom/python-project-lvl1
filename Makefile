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


build:
	poetry build


package-local-install:
	pip3 install --user --upgrade dist/*.whl


package-repo-install:
	pip install -i https://test.pypi.org/simple/ konstantin-hexlet-code --upgrade


upload-to-testpypi:
	poetry publish -r testPyPi --build --dry-run


lint:
	poetry run flake8 brain_games

