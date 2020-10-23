install:
	poetry install


brain-games:
	poetry run brain-games

build:
	poetry build

package-install:
	pip3 install --user --upgrade --no-warn-script-location dist/*.whl
