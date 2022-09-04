DIR=services/

mypy:
	pipenv run mypy --config-file mypy.ini services
pants-fmt:
	./pants --pants-config-files=pants.toml --changed-since=origin/main fmt
pants-lint:
	./pants --pants-config-files=pants.toml --changed-since=origin/main lint
runserver:
	pipenv run gunicorn  'server.app:app' --reload
test:
	pipenv run pytest ${DIR}
vulture:
	pipenv run vulture
