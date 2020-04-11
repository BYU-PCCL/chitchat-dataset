# Remove this Makefile after https://github.com/python-poetry/poetry/issues/241 

all:	install lint test

install:	## Install all the dependencies
	poetry install --no-root

mypy:	## Run mypy
	poetry run mypy chitchat_dataset

flake8:	## Run flake8
	poetry run flakehell lint

lint:	mypy flake8 ## Lint the code with mypy and flake8

test:	## Run the tests
	poetry run pytest --verbose

.version: version=required
.version:
	poetry version $(version)

.tag: CURRENT_VERSION=$(shell poetry version | sed "s/chitchat-dataset //")
.tag:
	git commit pyproject.toml -m $(CURRENT_VERSION)
	git tag -m $(CURRENT_VERSION) $(CURRENT_VERSION)

release:	.version .tag	## Bump the version as specified, e.g. `make release version=minor`
	@printf "\nIf everything looks ok, run 'git push --follow-tags' to publish the release\n"

# https://gist.github.com/prwhite/8168133#gistcomment-1716694
help:	## Show this help message
	@printf "$$(grep -hE '^\S+:.*##' $(MAKEFILE_LIST) | sed -e 's/:.*##\s*/:/' -e 's/^\(.\+\):\(.*\)/\\x1b[36m\1\\x1b[m:\2/' | column -c2 -t -s :)"

.PHONY: all install mypy flake8 lint test tag release help
